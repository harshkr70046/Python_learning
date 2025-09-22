#for loop
str = "Hello Harsh how are you ?"
for i in str:
    print(i)
str2 = str.rsplit()
for j in str2:
    print(j)
    for k in j:
        print(k)
for i in range(1,10):
    print(i)
for i in range(2,21,2):
    print(i)

# while loop
i = int(input("Enter any number = "))
while i<=30:
    print(i)
    i = int(input("Enter any number "))
else:
    print("opps you have enter greater number..")
