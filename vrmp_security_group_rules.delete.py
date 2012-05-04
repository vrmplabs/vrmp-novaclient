from novaclient.v1_1 import client


nt = client.Client('admin', 'admin', 'admin', 'http://localhost:5000/v2.0', service_type='compute')

grouplist = nt.security_groups.list()
print "Group list:"
for group in grouplist:
    print "id:" + str(group.id) + "    name:" + group.name + "    description:" + group.description
    for rule in group.rules:
        print rule

rule = raw_input("Please enter the rule:")
while not rule:
    rule = raw_input("Please enter the rule:")

nt.security_group_rules.delete(rule)
