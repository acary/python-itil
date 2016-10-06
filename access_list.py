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

phone1 = "Phone 1"
tablet1 = "Tablet 1"
laptop1 = "Laptop 1"
desktop1 = "Desktop 1"

# add and remove devices to networks

net1.append(phone1)
net1.append(tablet1)
net1.append(laptop1)
net1.pop()
net1.append(desktop1)

# display networks
print("Network 1:")
print(net1)


# system report

print("--- %s seconds ---" % (time.time() - start_time))

# exit

exit()
