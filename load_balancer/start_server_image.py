import virtualbox
import os

from helper_methods import copy_file

GUEST_TYPE_ID = u'Ubuntu_64'
VM_NAME = 'server_image'
CLONE_NAME = 'server_image_clone'

v_box = virtualbox.VirtualBox()
session = virtualbox.Session()

vm = v_box.find_machine(VM_NAME)
# vm_settings_path = vm.settings_file_path
# new_settings_path = os.path.join("\\".join(vm_settings_path.split("\\")[:-1]), CLONE_NAME+".vbox")
# copy_file(vm_settings_path, new_settings_path)

try:
    new_clone = v_box.find_machine(CLONE_NAME)
except virtualbox.library.VBoxError, e:
    print(e)
finally:
    new_clone = None

if not new_clone:
    new_clone = v_box.create_machine('', CLONE_NAME, [], GUEST_TYPE_ID, '')
    new_clone.save_settings()
    v_box.register_machine(new_clone)
    clone_progress = vm.clone_to(new_clone, virtualbox.library.CloneMode(1), [])
    # new_clone.

progress = new_clone.launch_vm_process(session, 'gui', '')

session.console.power_down()
