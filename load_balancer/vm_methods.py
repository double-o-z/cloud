from virtualbox.pool import MachinePool
from virtualbox import VirtualBox


def get_machines(base_name):
    v_box = VirtualBox()
    all_machines = v_box.machines
    machines = []
    for machine in all_machines:
        if base_name in machine.name:
            machines.append(machine)
    return machines


def launch_machine(machine):
    progress = machine.launch_vm_process(type_p='headless')
    progress.wait_for_completion(60 * 1000)


def create_session(machine):
    session = machine.create_session()
    return session


def guest_session(session, user_name, password):
    gs = session.console.guest.create_session(user_name, password)
    gs.wait_for(1, 15)
    return gs


def machine_execute(gs, command, args):
    process, stdout, stderr = gs.execute(command, args)
    return stdout


def power_down(session):
    p = session.console.power_down()
    p.wait_for_completion(60 * 1000)


def create_pool(base_name):
    return MachinePool(base_name)


def acquire(pool, user_name, password):
    return pool.acquire(user_name, password)


def execute(session, user_name, password, command, args):
    with session.console.guest.create_session(user_name, password) as gs:
        gs.wait_for(1, 60)
        _, out, _ = gs.execute(command, args)
        return out

# pool = MachinePool('server')
# sessions = []
# try:
#     for i in range(3):
#         sessions.append(pool.acquire("batman", "123"))
#
#     try:
#         for session in sessions:
#             with session.guest.create_session("batman", "123") as gs:
#                 _, out, _ = gs.execute("ifconfig")
#                 print(out)
#
#     except Exception as err:
#         print("Error raised on execute: %s" % err)
#
# except Exception as err:
#     print("Error raised on acquire: %s" % err)
#
# finally:
#     for session in sessions:
#         try:
#             pool.release(session)
#         except Exception as err:
#             print("Error raised on release: %s" % err)
