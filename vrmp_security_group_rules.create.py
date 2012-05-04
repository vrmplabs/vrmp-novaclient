from novaclient.v1_1 import client


nt = client.Client('admin', 'admin', 'admin', 'http://localhost:5000/v2.0', service_type='compute')

grouplist = nt.security_groups.list()
print "Group list:"
for group in grouplist:
    print "id:" + str(group.id) + "    name:" + group.name + "    description:" + group.description

parent_group_id = raw_input("Please enter the parent_group_id:")
while not parent_group_id:
    parent_group_id = raw_input("Please enter the parent_group_id:")

ip_protocol = raw_input("Please enter the ip_protocol(tcp/udp/icmp):")
while not ip_protocol:
    ip_protocol = raw_input("Please enter the ip_protocol(tcp/udp/icmp):")

from_port = raw_input("Please enter the from_port(TCP/UDP: Enter integer value between 1 and 65535. ICMP: enter a value for ICMP type in the range (-1: 255)):")
while not from_port:
    from_port = raw_input("Please enter the from_port(TCP/UDP: Enter integer value between 1 and 65535. ICMP: enter a value for ICMP type in the range (-1: 255)):")

to_port = raw_input("Please enter the to_port(TCP/UDP: Enter integer value between 1 and 65535. ICMP: enter a value for ICMP type in the range (-1: 255)):")
while not to_port:
    to_port = raw_input("Please enter the to_port(TCP/UDP: Enter integer value between 1 and 65535. ICMP: enter a value for ICMP type in the range (-1: 255)):")

group_id = raw_input("Please enter the group_id:")
if not group_id:
    group_id = None

cidr = raw_input("Please enter the cidr(Classless Inter-Domain Routing (e.g. 192.168.0.0/24)):")
if not cidr:
    cidr = '0.0.0.0/0'

nt.security_group_rules.create(parent_group_id, ip_protocol=ip_protocol, from_port=from_port, to_port=to_port, cidr=cidr, group_id=group_id)
