
# This program generated random password.
import string
import random


def pw_gen(size = 8, char = string.ascii_letters + string.digits + string.punctuation ):

    return "" .join(random.choice(char) for i in range(size) )
print(pw_gen(int(input('How many characters in your password? : '))))
