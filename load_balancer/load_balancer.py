# Create a pool of internal server clones.
# Collect urls for internal servers (example: ['10.0.3.1:8080', '10.0.3.2:8080', ...])
# Create an external server that exposes a different ip and port, such as: '10.0.0.1:5050'
# Create an OOP application that starts first instance of server image.
# Then, exposes the external ip, and returns a list of currently active clones (starts with 0).
# Create a method that retrieves currently active clones.
# Create a method that clones the server once, and adds the new clone to currently active clones list.
# Create a method that powers down a clone and (maybe even delete clone) removes from active clones list.

# Proceed to next tasks (create ui, etc..)
from helper_methods import get_ip_address
from vm_methods import get_machines, launch_machine, create_session, guest_session, machine_execute, power_down, \
    create_pool, acquire, execute

EXTERNAL_PORT = 5050
INTERNAL_PORT = 8080
BASE_NAME = "server"
USER_NAME = "batman"
PASSWORD = "123"


class LoadBalancer:
    def __init__(self):
        self.external_address = ''
        self.internal_addresses = []
        self.machines = []
        self.active_machines = []
        self.pool = None
        self.session = None

        self.get_external_address()
        # self.start_internal_external_server()
        # self.get_machines()
        # self.launch_machines()
        # self.get_internal_addresses()
        self.create_pool()
        self.create_session()
        self.execute()

        a = 0

    def get_external_address(self):
        self.external_address = get_ip_address(EXTERNAL_PORT)

    def start_internal_external_server(self):
        pass

    def get_machines(self):
        self.machines = get_machines(BASE_NAME)

    def launch_machines(self):
        for machine in self.machines:
            launch_machine(machine)
            self.active_machines.append(machine)

    def get_internal_addresses(self):
        command, args = "ifconfig", []
        for machine in self.active_machines:
            session = create_session(machine)
            try:
                gs = guest_session(session, USER_NAME, PASSWORD)
                output = machine_execute(gs, command, args)
                self.internal_addresses.append(output)
            except Exception as err:
                print(err)
                self.power_down(session)

    def power_down(self, session):
        power_down(session)

    def create_pool(self):
        self.pool = create_pool(BASE_NAME)

    def create_session(self):
        self.session = acquire(self.pool, USER_NAME, PASSWORD)

    def execute(self):
        command, args = "ifconfig", []
        result = execute(self.session, USER_NAME, PASSWORD, command, args)
        print(result)
