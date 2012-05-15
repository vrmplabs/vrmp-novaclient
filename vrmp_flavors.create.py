from novaclient.v1_1 import client


nt = client.Client('admin', 'admin', 'admin', 'http://localhost:5000/v2.0', service_type='compute')

# show flavorlist
flavoridlist = []
flavorlist = nt.flavors.list()
print "Flavor list:"
for flavor in flavorlist:
    print "id:" + flavor.id
    flavoridlist.append(int(flavor.id))

# get flavorid
usedefault = raw_input("Do you want to use the default flavor id(" + str(max(flavoridlist) + 1) + ")?(y/n):")
while usedefault not in ['y', 'n']:
    usedefault = raw_input("Do you want to use the default flavor id(" + str(max(flavoridlist) + 1) + ")?(y/n):")
if usedefault == 'y':
    flavorid = str(max(flavoridlist) + 1)
else:
    flavorid = raw_input("Please enter the flavor id:")
    while flavorid in flavoridlist:
       flavorid = raw_input("Please enter the flavor id:")

# get name
name = raw_input("Please enter the name:")
while not name:
    name = raw_input("Please enter the name:")

# get vcpus
vcpus = raw_input("Please enter the vcpus:")
while not vcpus:
    vcpus = raw_input("Please enter the vcpus:")

# get ram
ram = raw_input("Please enter the memory(MB):")
while not ram:
    ram = raw_input("Please enter the memory(MB):")

# get disk
disk = raw_input("Please enter the root disk(GB):")
while not disk:
    disk = raw_input("Please enter the root disk(GB):")

# get ephemeral
ephemeral = raw_input("Please enter the ephemeral disk(GB):")
if not ephemeral:
    ephemeral = 0

flavor = nt.flavors.create(name, ram, vcpus, disk, flavorid, ephemeral=ephemeral)

print "VRMP_info: Flavor '" + flavor.name + "' was created successfully."
