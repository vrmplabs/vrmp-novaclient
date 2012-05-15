from novaclient.v1_1 import client


nt = client.Client('admin', 'admin', 'admin', 'http://localhost:5000/v2.0', service_type='compute')

# show serverlist
serveridlist = []
serverlist = nt.servers.list()
print "Server list:"
for server in serverlist:
    print "id:" + server.id + "    name:" + server.name
    serveridlist.append(server.id)

# get server
server = raw_input("Please enter the server id:")
while server not in serveridlist:
    server = raw_input("Please enter the server id:")

# show floating_iplist
listlen = 0
floating_ipiplist = []
floating_iplist = nt.floating_ips.list()
print "Floating ip list:" 
for floating_ip in floating_iplist:
    if floating_ip.instance_id == None:
        print "pool:" + floating_ip.pool + "    ip:" + floating_ip.ip
        floating_ipiplist.append(floating_ip.ip)
        listlen = listlen + 1

createip = raw_input("Do you want to create a new floating ip?(y/n):")
while createip not in ['y', 'n']:
    createip = raw_input("Do you want to create a new floating ip?(y/n):")
if createip == 'y':
    # show floating_ip_poollist
    floating_ip_poolnamelist = []
    floating_ip_poollist = nt.floating_ip_pools.list()
    print "Floating ip pool list:"
    for floating_ip_pool in floating_ip_poollist:
        print "name:" + floating_ip_pool.name
        floating_ip_poolnamelist.append(floating_ip_pool.name)

    # get pool
    pool = raw_input("Please enter the pool name:")
    while pool and pool not in floating_ip_poolnamelist:
        pool = raw_input("Please enter the pool name:")

    nt.floating_ips.create(pool=pool)

    # show floating_iplist
    floating_ipiplist = []
    floating_iplist = nt.floating_ips.list()
    print "Floating ip list:"
    for floating_ip in floating_iplist:
        if floating_ip.instance_id == None:
            print "pool:" + floating_ip.pool + "    ip:" + floating_ip.ip
            floating_ipiplist.append(floating_ip.ip)
else:
    if listlen == 0:
        print "VRMP_warn: No floating ip was allocated, the system has been exit."
        exit()

# get address
address = raw_input("Please enter the address:")
while address not in floating_ipiplist:
    address = raw_input("Please enter the address:")

nt.servers.add_floating_ip(server, address)

print "VRMP_info: Floating ip was allocated successfully."
