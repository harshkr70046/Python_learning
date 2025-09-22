lis = [1,3,5,"kumar","Ram",False]

for i in lis:
    print(i)
lis1 = []
def list_input(lis1,size):
    i = 0
    while i<size:
        list_data = int(input("Enter any number = "))
        lis1.append(list_data)
        i+=1
    return lis1
size = int(input("Enter the size of list = "))
list_input(lis1,size)
lis1.pop()
print(lis1)
# lis1.sort() ascendind order
lis1.sort(reverse=True) #decending order
print(lis1)
lis1.reverse()
print(lis1)
print(lis1.index(4))
