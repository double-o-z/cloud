# cloud
A study purposes cloud exercise.
This project creates a load-balancer that "spawns" clones of a linux vm.
On each virtual machine, a service is started on boot.
The service starts a socket server, that listens to http requests.
Each said server, is multi-threaded, able to connect to up to 5 clients.
Therefore, upon need the load-balancer will spawn additional server.
Also, close redundant servers.
Cloning is done via pyvbox - python wrapper to VirtualBox Main API.

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
sudo cp server/server.service /lib/systemd/system/server.service
sudo systemctl enable server.service
sudo systemctl start server.service
sudo systemctl status server.service

To clone linux machine:
...