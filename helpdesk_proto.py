# Define help desk ticket classes

class Ticket():
    """ An example ticket structure """
    status = "unresolved"
    priority = 3
    department = "Accounting"

# Track tickets

queue = []


# Create ticket

x = Ticket()
queue.append(x)

y = Ticket()
queue.append(y)

# Print ticket queue

print(queue)

# Print reports

print(type(queue))
