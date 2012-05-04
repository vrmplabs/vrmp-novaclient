1.将.py文件放在安装了openstack的机器的任意路径下
2.执行命令：python ****.py，运行脚本
3.根据提示输入相关参数
4.参数说明：

vrmp_servers.create.py(创建虚拟机并得到id)：
name(虚拟机名称)：必须
image(镜像id)：必须 从列表得到值
flavor(flavorid)：必须 从列表得到值
userdata(userdata)：非必须
key_name(keypair名称)：非必须 从列表得到值 注意输入列表中现实的名称，不是id
security_groups(安全组名称)：非必须 从列表得到值，可以为多个值，半角逗号分割 注意输入列表中现实的名称，不是id