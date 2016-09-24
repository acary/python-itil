# Import libraries
import math
import random

# Define applications modules

def count_modules():
    i = 0

count_modules()

# Authentication and login

def sign_up(str):
    i = 0
    i += 1
    print(i)
    print("Welcome, " + str + "!")

def login(str):
    print(str + " has logged in!")

# Dashboard

def show_report(int):
    print("The system has " + str(int) + " processes.")

# Content window

def show_main(str):
    print([str])

# Messages

def send_msg(str):
    print("Sending: " + str)

def receive_msg(str):
    print("Received: " + str)

# Settings

def settings(str):
    print("Adjust your settings here, " + str)

# Show test output
test_seed = random.randint(1, 10)
results = math.exp(test_seed)
print("Results: " + str(results))

################
# Run Program
################

sign_up("Aurora")
login("Aurora")
show_report(4)
show_main("Here")
send_msg("Hello")
receive_msg("Hello")
settings("Bleep")
