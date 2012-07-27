from novaclient.v1_1 import client


nt = client.Client('admin', 'admin', 'admin', 'http://localhost:5000/v2.0', service_type='compute')

# get name
name = raw_input("Please enter the name:")
while not name:
    name = raw_input("Please enter the name:")

# show imagelist
imageidlist = []
imagelist = nt.images.list()
print "Image list:"
for image in imagelist:
    print "id:" + image.id + "    name:" + image.name
    imageidlist.append(image.id)

# get image
image = raw_input("Please enter the image id:")
while image not in imageidlist:
    image = raw_input("Please enter the iamge id:")

# show flavorlist
flavoridlist = []
flavorlist = nt.flavors.list()
print "Flavor list:"
for flavor in flavorlist:
    print "id:" + flavor.id + "    name:" + flavor.name
    flavoridlist.append(flavor.id)

# get flavor
flavor = raw_input("Please enter the flavor id:")
while flavor not in flavoridlist:
    flavor = raw_input("Please enter the flavor id:")

# get userdata
userdata = raw_input("Please enter the userdata:")

# show keypairlist
keypairnamelist = []
keypairlist = nt.keypairs.list()
print "Keypair list:"
for keypair in keypairlist:
    print "name:" + keypair.name
    keypairnamelist.append(keypair.name)

# get key_name
key_name = raw_input("Please enter the key name:")
while key_name and key_name not in keypairnamelist:
    key_name = raw_input("Please enter the key name:")

# show security_grouplist
security_groupnamelist = []
security_grouplist = nt.security_groups.list()
print "Security group list:"
for security_group in security_grouplist:
    print "name:" + security_group.name
    security_groupnamelist.append(security_group.name)

# get security_groups
security_groups = raw_input("Please enter the security group names:").split(',')
for security_group in security_groups:
    while security_group and security_group not in security_groupnamelist:
        security_groups = raw_input("Please enter the security group names:").split(',')

server = nt.servers.create(name, image, flavor, userdata=userdata, key_name=key_name, security_groups=security_groups)

print "VRMP_info: Server '" + server.name + "' is creating, the id is '" + server.id + "'."
