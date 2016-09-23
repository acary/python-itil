#

def main():
    print("Welcome to the Service Desk!")

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(100)



if __name__ == "__main__":
    main()
