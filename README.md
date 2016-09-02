# cloud
A study purposes cloud exercise, that creates instances of virtual machines running linux,
and creating http servers using python and socket package.

Systemd was used to place a unit that starts server.py on system boot.
The unit is placed at /lib/systemd/system/server.service
It is setup once with these command:
sudo systemctl enable server.service
sudo systemctl start server.service

To make sure server is running correctly, check service status:
sudo systemctl status server.service