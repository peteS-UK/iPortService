# iPortService
Send Home Assistant messages to LightSymphony iPort via UDP.  The iPort Command will accept area_on x, area_off x (x being the area number), all_on, all_off, inten_x_d (set intensity of area x to d - 1-10), start_show, stop_show and colour_x_c (set colour of area x to c - 1-16).  Either leave the iPort IP Address blank to attemp discovery, or manually specify the address.
