from novaclient.v1_1 import client


nt = client.Client('admin', 'admin', 'admin', 'http://localhost:5000/v2.0', service_type='compute')

# show security_grouplist
security_groupidlist = []
security_grouplist = nt.security_groups.list()
print "Security group list:"
for security_group in security_grouplist:
    print "id:" + str(security_group.id) + "    name:" + security_group.name + "    description:" + security_group.description
    security_groupidlist.append(str(security_group.id))

# get group
group = raw_input("Please enter the security group id:")
while group not in security_groupidlist:
    group = raw_input("Please enter the security group id:")

nt.security_groups.delete(group)

print "VRMP_info: Security group '" + group + "' was deleted successfully."
