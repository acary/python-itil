# import libraries
import random

# define states
s0 = "In service (operational)"
s1 = "Out of service"
s2 = "Updates required"
s3 = "Standby"

# define components

c0 = "Primary console"
c1 = "Secondary console"
c2 = "External router"
c3 = "Switch"
c4 = "Firewall"
c5 = "Load balancer"
c6 = "Internal router"

# assign component states

super_c0 = [c0, s0]
super_c1 = [c1, s3]
super_c2 = [c2, s0]
super_c3 = [c3, s1]
super_c4 = [c4, s0]
super_c5 = [c5, s0]
super_c6 = [c6, s0]

# check component states

print("System configuration report follows:\n")
print(super_c0)
print(super_c1)
print(super_c2)
print(super_c3)
print(super_c4)
print(super_c5)
print(super_c6)
