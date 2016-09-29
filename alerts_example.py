# import libraries
import random

# define states
s0 = "In service"
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

# check if any components include out-of-service states

super_components = [super_c0, super_c1, super_c2, super_c3, super_c4, super_c5, super_c6]

if s1 in super_c0:
    print("The " + str(c0) + " needs attention.")

if s1 in super_c1:
    print("The " + str(c1) + " needs attention.")

if s1 in super_c2:
    print("The " + str(c2) + " needs attention.")

if s1 in super_c3:
    print("The " + str(c3) + " needs attention.")

if s1 in super_c4:
    print("The " + str(c4) + " needs attention.")

if s1 in super_c5:
    print("The " + str(c5) + " needs attention.")

if s1 in super_c6:
    print("The " + str(c6) + " needs attention.")
