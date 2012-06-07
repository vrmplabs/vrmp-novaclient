from novaclient.v1_1 import client


nt = client.Client('admin', 'admin', 'admin', 'http://localhost:5000/v2.0', service_type='compute')

# get name
name = raw_input("Please enter the name:")
while not name:
    name = raw_input("Please enter the name:")

# get description
description = raw_input("Please enter the description:")
while not description:
    description = raw_input("Please enter the description:")

security_group = nt.security_groups.create(name, description)

print "VRMP_info: Security group '" + security_group.name + "' was created successfully."
