1.将.py文件放在安装了openstack的机器的任意路径下
2.执行命令：python ****.py，运行脚本
3.根据提示输入相关参数
4.参数说明：

vrmp_servers.create.py(创建虚拟机并得到id):
name(虚拟机名称):必须
image(镜像id):必须 从列表得到值
flavor(flavorid):必须 从列表得到值
userdata(userdata):非必须
key_name(keypair名称):非必须 从列表得到值 注意输入列表中现实的名称，不是id
security_groups(安全组名称):非必须 从列表得到值，可以为多个值，半角逗号分割 注意输入列表中现实的名称，不是id

vrmp_servers.add_floating_ip.py(为虚拟机添加floating ip):
server(虚拟机id):必须 从列表得到值
address(ip地址):必须 从列表得到值

vrmp_security_groups.create.py(创建安全组):
name(安全组名称):必须
description(安全组描述):必须

vrmp_security_groups.delete.py(删除安全组):
group(安全组id):必须 从列表得到值

vrmp_security_group_rules.create.py(创建安全组规则):
parent_group_id():必须 从列表得到值
ip_protocol():必须 tcp/udp/icmp三选一
from_port():必须 按提示范围整数
to_port():必须 按提示范围整数
group_id():非必须 从security group列表得到值
cidr():非必须 默认0.0.0.0/0

vrmp_security_group_rules.delete.py(删除安全组规则):
rule(规则id):必须 从列表得到值

vrmp_keypairs.create.py(创建key):
name(key名称):必须
public_key(导入的key值):非必须 从其他位置获得

vrmp_keypairs.delete.py(删除key):
key(key名称):必须 从列表得到值

vrmp_flavors.create.py(创建flavor):
flavorid(flavorid):必须 如果不用默认值，必须根据列表选择不存在的id
name(flavor名称):必须
vcpus(虚拟cpu个数):必须
ram(内存大小MB):必须
disk(root磁盘大小GB):必须
ephemeral(ephemeral磁盘大小GB):非必须 默认0

vrmp_flavors.delete.py(删除flavor):
flavor(flavorid):必须 从列表得到值