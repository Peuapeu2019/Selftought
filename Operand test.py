def main():

    name = input(" enter name: ")


    num = input("Enter a number: ")

    mod = int(num, 10) %2

    if mod > 0:

        print("You picked an odd number.")
    else:

        print("You picked an even number.")

    num1 = (input("Enter another number to check : "))

    check = int(input(" enter number to divide: "))

    if int(num1) % 4 == 0:
        print( num1+ " is a multiple of 4 : " )

    elif int(num1) % 2 == 0:
        print(num1 + " is even number " +str(check))
    else:
        print(num1+ " is an odd number: ")

    num = int(input(" Enter a number between 0 to 90:  "))

    newList = []
    for i in newList:

        if i < num:
            newList.append(i)
            print(newList)


main()