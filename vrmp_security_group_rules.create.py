from novaclient.v1_1 import client


nt = client.Client('admin', 'admin', 'admin', 'http://localhost:5000/v2.0', service_type='compute')

# show security_grouplist
security_groupidlist = []
security_grouplist = nt.security_groups.list()
print "Security group list:"
for security_group in security_grouplist:
    print "id:" + str(security_group.id) + "    name:" + security_group.name + "    description:" + security_group.description
    security_groupidlist.append(str(security_group.id))

# get parent_group_id
parent_group_id = raw_input("Please enter the parent group id:")
while parent_group_id not in security_groupidlist:
    parent_group_id = raw_input("Please enter the parent group id:")

# get ip_protocol
ip_protocol = raw_input("Please enter the ip protocol(tcp/udp/icmp):")
while ip_protocol not in ['tcp', 'udp', 'icmp']:
    ip_protocol = raw_input("Please enter the ip protocol(tcp/udp/icmp):")

# get from_port
from_port = raw_input("Please enter the from port(TCP/UDP: Enter integer value between 1 and 65535. ICMP: enter a value for ICMP type in the range (-1: 255)):")
while not from_port:
    from_port = raw_input("Please enter the from port(TCP/UDP: Enter integer value between 1 and 65535. ICMP: enter a value for ICMP type in the range (-1: 255)):")

# get to_port
to_port = raw_input("Please enter the to port(TCP/UDP: Enter integer value between 1 and 65535. ICMP: enter a value for ICMP type in the range (-1: 255)):")
while not to_port:
    to_port = raw_input("Please enter the to port(TCP/UDP: Enter integer value between 1 and 65535. ICMP: enter a value for ICMP type in the range (-1: 255)):")

# get group_id
group_id = raw_input("Please enter the group id:")
while group_id and group_id not in security_groupidlist:
    group_id = raw_input("Please enter the group id:")

# get cidr
cidr = raw_input("Please enter the cidr(Classless Inter-Domain Routing (e.g. 192.168.0.0/24)):")
if not cidr:
    cidr = '0.0.0.0/0'

rule = nt.security_group_rules.create(parent_group_id, ip_protocol=ip_protocol, from_port=from_port, to_port=to_port, cidr=cidr, group_id=group_id)

print "VRMP_info: Security group rule '" + rule.name + "' was created successfully."
