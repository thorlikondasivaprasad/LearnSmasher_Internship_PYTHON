#    CURRENCY CONVERTER

import sys

def dollars_to_euros(dol):
    euro=(0.94*dol)
    return euro

def dollars_to_rupees(dol):
    rupees=(82.63*dol)
    return rupees

def dollars_to_pounds(dol):
    pound=(0.81*dol)
    return pound

def dollars_to_australianpound(dol):
    aus_dollar=(1.52*dol)
    return aus_dollar

while(True):
    print("----------------------------------------------------------------------------------")

    print("Choose the Options \n 1.Dollars_to_Euros \n2.Dollars_to_Rupees \n3.Dollars_to_Pounds \n4.Dollars_to_AustraliaPounds \n5.Quit from game\n")

    inp=input("Enter the choice to convert CURRENCY : \n")
    choice=int(inp)

    if (choice==1):
        dollar=int(input("Enter the Dollar Amount to Convert :  \n"))
        print("The amount in Euros is : ",dollars_to_euros(dollar))

    elif (choice==2):
        dollar=int(input("Enter the Dollar Amount to Convert :  \n"))
        print("The amount in Rupees is : ",dollars_to_rupees(dollar))

    elif (choice==3):
        dollar=int(input("Enter the Dollar Amount to Convert :  \n"))
        print("The amount in Pounds is : ",dollars_to_pounds(dollar))

    elif (choice==4):
        dollar=int(input("Enter the Dollar Amount to Convert :  \n"))
        print("The amount in Australian dollars is : ",dollars_to_australianpound(dollar))

    elif (choice==5):
        break

print("Thank you for Playing ................😊")
