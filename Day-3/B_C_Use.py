# break and continue statemant
for i in range(10):
    if(i==7):
        continue
    print(i,end=",")


sum = 0
count = 0
while True:
    num = int(input("\nEnter any number = "))
    sum+=num
    count+=1
    if num==0:
        break
print("Sum of  given number = ",sum)
print("total number = ",count)
print("Average of all number = ",(sum//count))