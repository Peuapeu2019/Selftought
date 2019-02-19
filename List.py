from array import *
from random import *
#write a program that prints out all the elements of the list that are less than 5.
numList = array("i",[1,2,3,4,5,8,13,21,34,55,89])
for numList in range(0 , 5):
  print(numList)
# 3.Ask the user for a number and return a list that contains only elements from the original list a that are smaller
# than that number given by the user.
List = array("i",[1,2,3,4,5,8,13,21,34,55,89])
num = int(input("Please enter a new number between 0 to 90:  "))

newList = []

for i in List:
    if i < num:
        newList.append(i)

print(newList)

#Take two lists and write a program that returns element that are common between the list.
#Make sure your programm works on different list sizes.

a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,21]

print("List a: " +str(a), "List B:" +str(b))

emptyA = []
for i in b:
    if i in a:
        print("The common number between two list is: " + str(i))

#Ask user for a string and print out whether the string is a Palindrome or not.

print("is this a list of Palindrome or not? : ")
word = input("please enter a word: ")
word = str(word)
rvs = word[::-1]
print(rvs)
if word == rvs:
    print("This is a Palindrome ")
else:
    print("This is not a palindrome")
