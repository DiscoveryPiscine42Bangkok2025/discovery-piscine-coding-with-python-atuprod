def main(): 
    for i in range(0,11):
        print("Table de " + str(i) +":",end='')
        for j in range(0,11):
            print(i * j,end=' ')
        print("")
main()
