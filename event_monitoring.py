# Import libraries
import random

# Define processes
i = random.randint(1, 10)

p1 = i**2

# Detect event
queue = 0
if (p1 >= 25):
    queue = 1
    e = "An event occurred"
else:
    pass

# Alert event
if (queue == 1):
    if (e):
        print(e)
else:
    print("No events exist")

exit()
