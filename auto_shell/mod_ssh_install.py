import ConfigParser
import paramiko

import mod_print_logs


# ssh_install
def ssh_install():
    # config init
    config = ConfigParser.ConfigParser()
    config.readfp(open('config.ini'))

    # server create parameters
    key_path = config.get('server_create', 'key_path')
    key_name = config.get('server_create', 'key_name')
    floating_ip = config.get('server_create', 'floating_ip')

    # ssh install parameters
    ssh_username = config.get('ssh_install', 'ssh_username')
    public_key_url = config.get('ssh_install', 'public_key_url')
    public_key_save_path = config.get('ssh_install', 'public_key_save_path')
    base_repo_url = config.get('ssh_install', 'base_repo_url')
    epel_repo_url = config.get('ssh_install', 'epel_repo_url')
    repo_save_path = config.get('ssh_install', 'repo_save_path')

    # ssh connect
    ssh_key = paramiko.RSAKey.from_private_key_file('%s%s.pem' % (key_path, key_name))
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname = floating_ip, username = ssh_username, pkey = ssh_key)

    # ssh public key write
    ssh.exec_command('if [ ! -d %s ]; then mkdir %s; fi' % (public_key_save_path, public_key_save_path))
    ssh.exec_command('wget %s%s.pub -P %s' % (public_key_url, key_name, public_key_save_path))
    ssh.exec_command('if [ ! -d /work/ ]; then mkdir /work/; fi')
    ssh.exec_command('if [ ! -d /work/.ssh/ ]; then mkdir /work/.ssh/; fi')
    ssh.exec_command('while read line; do echo $line >> /work/.ssh/authorized_keys; done < %s%s.pub' % (public_key_save_path, key_name))
    print 'Public key write completed successfully!'

    # ssh yum update
    print 'Yum update is starting...'
    ssh.exec_command('rm -rf %s*' % repo_save_path)
    ssh.exec_command('wget %s -P %s' % (base_repo_url, repo_save_path))
    ssh.exec_command('wget %s -P %s' % (epel_repo_url, repo_save_path))
    stdin, stdout, stderr = ssh.exec_command('yum -y update')
    mod_print_logs.print_logs(stdout.readlines())

    # ssh puppet install
    print 'Puppet install is starting...'
    stdin, stdout, stderr = ssh.exec_command('yum -y install puppet')
    mod_print_logs.print_logs(stdout.readlines())

    # ssh close
    ssh.close()
