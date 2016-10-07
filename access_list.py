# import libraries
import time

start_time = time.time()

# networks

net1 = []
net2 = []
net3 = []
net4 = []
net5 = []

networks = [net1, net2, net3, net4, net5]

# devices

# phone1 = "Phone 1"
# tablet1 = "Tablet 1"
# laptop1 = "Laptop 1"
# desktop1 = "Desktop 1"

phone = {'Make': 'Phone', 'Model': 6564, 'IP': '192.168.1.1'}
tablet = {'Make': 'Tablet', 'Model': 6468, 'IP': '192.168.1.2'}
laptop = {'Make': 'Laptop', 'Model': 1264, 'IP': '192.168.1.3'}
desktop = {'Make': 'Desktop', 'Model': 6494, 'IP': '192.168.1.4'}

# add and remove devices to networks

""" net1.append(phone1)
net1.append(tablet1)
net1.append(laptop1)
net1.pop()
net1.append(desktop1) """

# Create functions to add or remove devices

def add_to_network(device, network):
    """ add device to network """
    network.append(device)

def drop_from_network(device, network):
    """ drop device from network """
    network.remove(device)

# Add device to network
add_to_network(phone, net1)
add_to_network(tablet, net1)
add_to_network(laptop, net1)
add_to_network(desktop, net1)

# Remove device from network
drop_from_network(phone, net1)

# Display network
print(net1)


# system report

print("--- %s seconds ---" % (time.time() - start_time))

# exit

exit()
