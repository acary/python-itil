# Import libraries
from datetime import date, time, datetime


# Main section

def main():
    # Get current date and time
    today = date.today()
    currenttime = datetime.now()

    # Greet the visitor
    print("Welcome to the Service Desk!")
    print("Today is: " + str(today))
    print("The time is: " + str(currenttime))

# Fibinacci sequence as a header
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(100)





# Run main
if __name__ == "__main__":
    main()
