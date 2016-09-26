import virtualbox

vbox = virtualbox.VirtualBox()
session = virtualbox.Session()
machine = vbox.find_machine("image")
machine.launch_vm_process(session, 'headless', '')

with session.console.guest.create_session("batman", "123") as gs:
    process, out, err = gs.execute("/bin/echo", ["bamba"])
    print(out)
