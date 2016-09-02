# cloud
A study purposes cloud exercise, that creates instances of virtual machines running linux,
and creating http servers using python and socket package.

Systemd was used to place a unit that starts server.py on system boot.
The unit is placed at /lib/systemd/system/server.service:
sudo cp server.service /lib/systemd/system/server.service
It is setup once with these command:
sudo systemctl enable server.service
sudo systemctl start server.service

To make sure server is running correctly, check service status:
sudo systemctl status server.service


To create the server image:

sudo apt-get install virtualenv
git clone git@github.com:double-o-z/cloud.git
virtualenv cloud
cd cloud && source bin/activate
pip install -r reqs.txt
sudo cp server.service /lib/systemd/system/server.service
sudo systemctl enable server.service
sudo systemctl start server.service
sudo systemctl status server.service