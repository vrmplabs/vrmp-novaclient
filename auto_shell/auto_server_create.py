import time

import mod_server_create
import mod_ssh_puppet_install


mod_server_create.server_create()
time.sleep(90)
mod_ssh_puppet_install.ssh_puppet_install()
