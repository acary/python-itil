# Import libraries
from random import randint

# Define business attributes
class Business:
    name = "Company name"
    industry = "Industry"
    size = "Size"
    revenue = 1000000

# Define business challenges
challenges  = []

# App hosting
challenges.append("App Cloud Hosting")

# Cloud data storage
cloud_storage = ["Amazon AWS", "Microsoft Azure"]
challenges.append(cloud_storage)

# Analytics
analytics = ["Application Performance Monitoring", "Network Analysis", "Data Storage Analysis"]
challenges.append(analytics)


# Display business challenges

print(challenges)

# Test ticket identification
ticket_no = randint(0, 9)

if (len(challenges) > 0):
    print("Services are required to address challenges. The ticket number is " + str(ticket_no) + ".")
