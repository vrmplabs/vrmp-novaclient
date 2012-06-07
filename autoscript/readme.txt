1.将文件夹放在安装了openstack的机器的任意路径下
2.执行命令：python auto_****.py，运行脚本
3.主要功能：创建keypair，创建虚拟机，分配floating ip，虚拟机安装puppet，虚拟机work添加公钥
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

[ssh_puppet_install]
ssh_username = 虚拟机用户名
repo_save_path = 保存repo的路径
repo_1_url = 下载repo的url
repo_2_url = 下载repo的url
public_key_save_path = 公钥存放路径
public_key_url = 下载公钥的url(只到目录)