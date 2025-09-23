#find the factorial of a number
num = int(input("Enter any number = "))
def factorial(num):
    if(num==0 | num==1):
        return 1
    return num*factorial(num-1)
print(f"factorial of {num} is = ",factorial(num))

#find the nth fibonachi number
def febonachi(num):
    if(num==0):
        return 0
    if(num==1):
        return 1
    
    return febonachi(num-1)+febonachi(num-2)

print(f"Fibonachi of {num}th is = ",febonachi(3))