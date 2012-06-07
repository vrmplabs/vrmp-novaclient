from novaclient.v1_1 import client


nt = client.Client('admin', 'admin', 'admin', 'http://localhost:5000/v2.0', service_type='compute')

# show keypairlist
keypairnamelist = []
keypairlist = nt.keypairs.list()
print "Keypair list:"
for keypair in keypairlist:
    print "name:" + keypair.name
    keypairnamelist.append(keypair.name)

# get key
key = raw_input("Please enter the key name:")
while key not in keypairnamelist:
    key = raw_input("Please enter the key name:")

nt.keypairs.delete(key)

print "VRMP_info: Keypair '" + key + "' was deleted successfully."
