#function in python 
#make a function of finding geometric mean of two number
def find_Geo_mean(a,b):
    mul = a*b
    sum = a+b
    return mul/sum
a = int(input("Enter first number = "))
b = int(input("Enter second number = "))
c = find_Geo_mean(a,b)
print("Geometric Mean of Two Number is = ",c)

def argumentTuple(*number):
    sum = 0
    count = 0
    for i in number:
        sum+=i
        count+=1
    return sum/count

temp = argumentTuple(5,7,8,9)
print(temp)
