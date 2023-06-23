"""Example of a custom component exposing a service."""
from __future__ import annotations

import logging
import socket


from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers.typing import ConfigType

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "iport_service"
_LOGGER = logging.getLogger(__name__)


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the sync service example component."""

    def my_service(call: ServiceCall) -> None:
        """My first service."""
        _LOGGER.debug('Received data %s', call.data)

        iPortIp = call.data.get("iPortIp")

        if (iPortIp is None):
            #No IP specified, so try discovery
            _LOGGER.debug('Discovery Started')
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

            try:
                sock.settimeout(2.0)
                sock.sendto(b"\x00\x01\x00\xF6", ('255.255.255.255', 30718))
                data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
            except (socket.error, socket.timeout):
                _LOGGER.debug ("Discovery Failure.")
                sock.close()
                return False
            else:
                _LOGGER.debug("Broadcast Response: %s", data)
                iPortIp = str(addr[0])
                _LOGGER.debug ("Discovered iPort IP: %s",iPortIp)
            finally:
                sock.close()

        _LOGGER.debug("iPortIp: %s", str(iPortIp))

        if (iPortIp is None):
            _LOGGER.debug('iPort IP Unknown.  Please specify iPort IP')
            return False

        message = call.data.get("iPortCommand") + "\r\n"

        iPortPort = 10001

        sock = socket.socket(socket.AF_INET, # Internet
                            socket.SOCK_DGRAM) # UDP

        try:
            sock.sendto(message.encode(), (iPortIp, iPortPort))
        except (socket.error, socket.timeout):
            _LOGGER.debug  ("Send Failure.")
            sock.close()
            return False
        else:
            _LOGGER.debug  ("Message %s sent", message)
        finally:
            sock.close()


    # Register our service with Home Assistant.
    hass.services.register(DOMAIN, 'iport', my_service)

    # Return boolean to indicate that initialization was successfully.
    return True
