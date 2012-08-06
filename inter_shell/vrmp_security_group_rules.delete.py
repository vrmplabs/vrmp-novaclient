from novaclient.v1_1 import client


nt = client.Client('admin', 'admin', 'admin', 'http://localhost:5000/v2.0', service_type='compute')

# show security_grouplist
ruleidlist = []
security_grouplist = nt.security_groups.list()
print "Security group list:"
for security_group in security_grouplist:
    print "id:" + str(security_group.id) + "    name:" + security_group.name + "    description:" + security_group.description
    for rule in security_group.rules:
        print "rule id:" + str(rule['id']) + "    ip protocol:" + rule['ip_protocol'] + "    from port:" + str(rule['from_port']) + "    to port:" + str(rule['to_port']) + "    source:" + str(rule['ip_range'])
        ruleidlist.append(str(rule['id']))

# get rule
rule = raw_input("Please enter the rule id:")
while rule not in ruleidlist:
    rule = raw_input("Please enter the rule id:")

nt.security_group_rules.delete(rule)

print "VRMP_info: Security group rule '" + rule + "' was deleted successfully."
