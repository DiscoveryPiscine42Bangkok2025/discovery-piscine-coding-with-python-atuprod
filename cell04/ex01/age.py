def main():
    x = int(input("Please tell me your age: "))
    print("You are currently " + str(x) + " years old.")
    for i in range(10,31,10):
        print("In "+ str(i) +" years, you'll be " + str(x + i) + " years old.")
main()
