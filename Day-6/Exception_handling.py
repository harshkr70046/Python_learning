a = input("Enter the number = ")
print(f"multiplication table of {a}")
try:
    for i in range(10):
        print(f"{int(a)}X{i+1}={int(a)*(i+1)}")

except:
    print("invalid input")
print("end of program")

try:
    num = int(input("Enter index = "))
    li = [7,9]
    print(li[num])
except ValueError:
    print("You have not entered int value.")
except IndexError:
    print("index out of range")


