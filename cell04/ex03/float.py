def main(): 
    x = float(input("Give me a number: "))
    if x.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
main()
