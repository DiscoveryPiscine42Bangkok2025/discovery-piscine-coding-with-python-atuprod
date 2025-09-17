def main():
    x = int(input("Enter a number less than 25\n"))
    if x < 25:
        while x <= 25:
            print("Inside the loop, my variable is",x)
            x += 1
    else:
        print("error")
main()
