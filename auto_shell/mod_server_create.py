import ConfigParser
import os
import time

from novaclient.v1_1 import client


# server_create
def server_create():
    # config init
    config = ConfigParser.ConfigParser()
    config.readfp(open('config.ini'))

    # nova auth parameters
    os_username = config.get('nova_auth', 'os_username')
    os_password = config.get('nova_auth', 'os_password')
    os_tenant_name = config.get('nova_auth', 'os_tenant_name')
    os_auth_url = config.get('nova_auth', 'os_auth_url')

    # server create parameters
    key_path = config.get('server_create', 'key_path')
    key_name = config.get('server_create', 'key_name')
    key_save_url = config.get('server_create', 'key_save_url')
    name = config.get('server_create', 'name')
    image = config.get('server_create', 'image')
    flavor = config.get('server_create', 'flavor')
    security_groups = config.get('server_create', 'security_groups').split(',')
    pool = config.get('server_create', 'pool')

    # client init
    nt = client.Client(os_username, os_password, os_tenant_name, os_auth_url, service_type = 'compute')

    # keypair create
    keypair = nt.keypairs.create(key_name)

    # write key file
    os.popen('if [ ! -d %s ]; then mkdir %s; fi' % (key_path, key_path))
    os.popen('echo "%s" > %s%s.pem' % (keypair.private_key, key_path, key_name))
    os.popen('echo "%s" > %s%s.pub' % (keypair.public_key, key_path, key_name))
    os.popen('scp -r %s %s' % (key_path, key_save_url))

    # server create
    server = nt.servers.create(name, image, flavor, key_name = key_name, security_groups = security_groups)

    # floating ip create
    floating_ip = nt.floating_ips.create(pool = pool)

    # write floating ip
    config_file = open('config.ini', 'w')
    config.set('server_create', 'floating_ip', floating_ip.ip)
    config.write(config_file)
    config_file.close()

    time.sleep(10)

    # add floating ip
    nt.servers.add_floating_ip(server.id, floating_ip.ip)

    print 'Instance "%s" is launching, please wait...' % name
