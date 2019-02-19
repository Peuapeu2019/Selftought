def endL():
#write a program that take a list and make a new list with the end number.

    X=[5, 10, 15, 20, 25]
    newList=[]
    for i in set(X):
        newList.append([X[0], X[-1]])
    print(newList)


endL()

import random
a = random.sample(range(30), 15)
print(a)
def smalllist(a):
    b = []
    b.append(a [0])
    b.append(a[(len(a)-1)])
    print(smalllist(a))