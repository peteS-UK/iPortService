# LightSymphony iPort Service for Home Assistant

## Archived

This repo is archived and replaced by a full switch component at [iPort](https://github.com/peteS-UK/iport)


[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)

This repo contains a Home Assistant integration for LightSymphony iPort contoller.  The report allows you to send simple UDP messages to areas on and off.

## Installation

The preferred installation approach is via Home Assistant Community Store - aka [HACS](https://hacs.xyz/).  The repo is installable as a [Custom Repo](https://hacs.xyz/docs/faq/custom_repositories) via HACS.

If you want to download the integration manually, create a new folder called iport_service under your custom_components folder in your config folder.  If the custom_components folder doesn't exist, create it first.  Once created, download the 3 files from the [github repo](https://github.com/peteS-UK/iPortService/tree/main/custom_components/iport_service) into this iport_service folder.

Once downloaded either via HACS or manually, restart your Home Assistant server.

## Configuration

To enable the integration, add the following line to your configuration.yaml file, typically in your /config folder.

```yaml
iport_service:
```

Once updated, restart your Home Assistant server again to enable the integration.

## Permitted commands

You can send the following commands to the iPort

| Command    | Description                                                                       |
|------------|-----------------------------------------------------------------------------------|
| all_on     | Whole garden ON                                                                   |
| all_off    | Whole garden OFF                                                                  |
| area_on x  | Switch ON an ‘area’, zone or scene, depending on what was stored in the receiver  |
| area_off x | Switch OFF an ‘area’, zone or scene, depending on what was stored in the receiver |
| inten_x_d  | ‘x’ = zone number, output intensity (dim level) ‘d’ = intensity 1-10              |
| start_show | Start the Light Show running (for colour LEDs)                                    |
| stop_show  | Stop the Light Show running                                                       |
| colour_x_c | ‘x’ = zone number, ‘c’ = colour code 1-16                                         |

## iPort Discovery

If you don't specify the IP address of the iPort in your integration, the service will attempt discover the iPort through broadcast.  This discoery won't work if the iPort is on a different subnet.  If discovery fails, you need to specify the IP address of the iPort in the integration.
