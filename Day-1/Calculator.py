a = int(input("Enter First number = "))
b = int(input("Enter Second number = "))
c = str(input("Enter Symboll = "))
if c=="+":
    print("Sum of two number is = " ,a+b)
elif c=="-":
    print("Subtract of two number is = " ,a-b)
elif c=="*":
    print("Multiply of two number is = " ,a*b)
elif c=="/":
    print("Divide of two number is = " ,a/b)
elif c=="//":
    print("Floor division of two number is = " ,a//b)
elif c=="%":
    print("Module of two number is = " ,a%b)
elif c=="**":
    print("Power of a and b = " ,a**b)
else:
    print("You have enter wrong operator")






