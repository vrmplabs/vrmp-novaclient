1.将文件夹放在安装了openstack的机器的任意路径下
2.执行命令：python auto_server_create.py，运行脚本
3.主要功能：创建keypair，创建虚拟机，分配floating ip，虚拟机/work目录添加公钥，虚拟机配置yum的repo，虚拟机安装libxp包，虚拟机下载并安装maya，虚拟机破解maya。
4.配置文件说明：
[nova_auth]
os_username = nova登录用户名
os_password = nova登录密码
os_tenant_name = nova使用的projectid
os_auth_url = nova验证url

[server_create]
key_path = keypair保存路径
key_name = keypair名称
key_save_url = 保存keypair服务器的ip和路径
name = 虚拟机名称
image = 镜像id
flavor = flavorid
security_groups = 安全组名称
pool = floating ip池
floating_ip = 生成的floating ip(无需配置)

[ssh_install]
ssh_username = 虚拟机用户名
public_key_url = 下载公钥的url(只到目录)
public_key_save_path = 公钥存放路径
base_repo_url = 下载基本repo的url
epel_repo_url = 下载扩展repo的url
repo_save_path = 保存repo的路径
maya_url = 下载maya安装文件的url
maya_name = maya安装文件的名称
maya_save_path = 保存maya安装文件的路径
maya_folder_path = 解压后maya文件夹的路径
maya_folder_name = 解压后maya文件夹的名称