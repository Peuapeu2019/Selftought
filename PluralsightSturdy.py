
def main():
    #get user name

    name = input(" Enter you name: ")

    #Get user age
    age = int(input(" Enter your age: "))

    #Get user year and tell what year user will be 100 year old
    year = str(( 2019 - age)+ 100)

    print(" Hi " +name+ " you will be 100 year old in: "+ year)

    #Add or Even practice.

    num = input("Enter a number: ")

    mod = int(num,10) % 2

    if mod > 0:
        print("You picked an odd number.")

    else:

        print("You picked an even number.")

    # print(num+ " divided by 2 = : " + x )




    "hello" .capitalize()== " Hello"
    "hello".replace("e", "a") == "hallo"
    "hello".isalpha() == 'true'
    "123" .isdigit() == "true" #not useful when converting to int.
    "some, csv, value" .split(", ") ==("some","csv", "value")
    
main()

