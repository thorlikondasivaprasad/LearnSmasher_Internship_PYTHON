import random as ran

small="abcdefghijklmnopqrstuvwxyz"

large="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

numbers="0123456789"

special_char="!@#$%^&*()"

password=small+large+numbers+special_char

size=int(input("Enter the size of Password : "))

print("".join(ran.sample(password,size)))
