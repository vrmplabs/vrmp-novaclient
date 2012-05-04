from novaclient.v1_1 import client


nt = client.Client('admin', 'admin', 'admin', 'http://localhost:5000/v2.0', service_type='compute')

# get name
name = raw_input("Please enter the name:")
while not name:
    name = raw_input("Please enter the name:")

# show imagelist
imagelist = nt.images.list()
print "Image list:"
for image in imagelist:
    print "id:" + str(image.id) + "    name:" + image.name

# get image
image = raw_input("Please enter the image:")
while not image:
    image = raw_input("Please enter the iamge:")

# show flavorlist
flavorlist = nt.flavors.list()
print "Flavor list:"
for flavor in flavorlist:
    print "id:" + str(flavor.id) + "    name:" + flavor.name

# get flavor
flavor = raw_input("Please enter the flavor(Size of image to launch.):")
while not flavor:
    flavor = raw_input("Please enter the flavor(Size of image to launch.):")

# get userdata
userdata = raw_input("Please enter the userdata:")

# show keypairlist
keypairlist = nt.keypairs.list()
print "Keypair list:"
for keypair in keypairlist:
    print "name:" + str(keypair.name)

# get key_name
key_name = raw_input("Please enter the key_name(Which keypair to use for authentication.):")

# show security_grouplist
security_grouplist = nt.security_groups.list()
print "Security_group list:"
for security_group in security_grouplist:
    print "id:" + str(security_group.id) + "    name:" + security_group.name

# get security_groups
security_groups = raw_input("Please enter the security_groups(Launch instance in these security groups.):").split(',')

server = nt.servers.create(name, image, flavor, userdata=userdata, key_name=key_name, security_groups=security_groups)

print "Server " + server.name + " is creating, the id is '" + str(server.id)+"'."
