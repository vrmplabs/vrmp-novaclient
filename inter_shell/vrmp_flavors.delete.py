from novaclient.v1_1 import client


nt = client.Client('admin', 'admin', 'admin', 'http://localhost:5000/v2.0', service_type='compute')

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

nt.flavors.delete(flavor)

print "VRMP_info: Flavor '" + flavor + "' was deleted successfully."
