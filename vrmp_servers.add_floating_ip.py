from novaclient.v1_1 import client


nt = client.Client('admin', 'admin', 'admin', 'http://localhost:5000/v2.0', service_type='compute')

# show serverlist
serverlist = nt.servers.list()
print "Server list:"
for server in serverlist:
    print "id:" + str(server.id) + "    name:" + server.name

# get server
server = raw_input("Please enter the server:")
while not server:
    server = raw_input("Please enter the server:")

# show floating_iplist
floating_iplist = nt.floating_ips.list()
print "Floating_ip list:"
for floating_ip in floating_iplist:
    print "id:" + str(floating_ip.id) + "    name:" + floating_ip.name

# get address
address = raw_input("Please enter the address:")
while not address:
    address = raw_input("Please enter the address:")

nt.servers.add_floating_ip(server, address)
