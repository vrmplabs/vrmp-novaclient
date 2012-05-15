from novaclient.v1_1 import client


nt = client.Client('admin', 'admin', 'admin', 'http://localhost:5000/v2.0', service_type='compute')

# get name
name = raw_input("Please enter the name:")
while not name:
    name = raw_input("Please enter the name:")

# get public_key
public_key = raw_input("Please enter the public key:")

keypair = nt.keypairs.create(name, public_key=public_key)

print "VRMP_info: Keypair '" + keypair.name + "' was created successfully."
