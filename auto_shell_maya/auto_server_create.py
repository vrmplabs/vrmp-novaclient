import time

import mod_server_create
import mod_ssh_install


mod_server_create.server_create()
time.sleep(90)
mod_ssh_install.ssh_install()
time.sleep(45)
mod_ssh_install.ssh_install_step2()
mod_ssh_install.ssh_install_step3()
mod_ssh_install.ssh_install_step4()
