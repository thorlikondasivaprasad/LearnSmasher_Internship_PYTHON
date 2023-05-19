def celsius_to_fahrenheit():

    print("Enter the fahrenheit degrees of temparature to convert celsius:\n")
    f=int(input())
    cels=(f-32)/(1.8)
    return cels
def fahrenheit_to_celsius():

    print("Enter the celsius degrees of temparature to convert fahrenheit:\n")
    c=int(input())
    f=(c*1.8)+32
    return f
print("Temparature Conversion between Celsius and Fahrenheit")
while(True):
    print("Enter the choice : \n1.celsius_to_fahrenheit \n2.fahrenheit_to_celsius \n3.Exit\n")
    c=int(input())
    if c==1:
        print("Degrees:",celsius_to_fahrenheit())
    elif c==2:
        print("Degrees:",fahrenheit_to_celsius())
    else:
        break
