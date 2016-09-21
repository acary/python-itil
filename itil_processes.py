# Variables include the 5 phases of the ITIL lifecycle
ss = "Service Strategy"
sd = "Service Design"
st = "Service Transition"
so = "Service Operation"
ci = "Continuous Integration"

# Print each phase
print("The five stages of service management according to ITIL are:\n")
print(ss)
print(sd)
print(st)
print(so)
print(ci)

# Array with five phases
itil = [ss, sd, st, so, ci]

# Print array
print(itil)

# IF statement
if itil[0] == ss:
    print("Let's start with Service Strategy")
else:
    print("It all starts with strategy...")

# For loop
for phases in itil:
    print(phases)

# Exit the program
exit()
