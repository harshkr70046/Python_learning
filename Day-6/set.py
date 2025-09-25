s = {1,2,3,4,5,6}
print(type(s))
# union prints unique data only from both set
s1 = {1,2,5,6,3}
s2 = {3,7,8,6}
print(s1.union(s2))
# print(s1,s2)
# s2.update(s1)
print(s1,s2)
# same elemnt
s3 = s1.intersection(s2)
print(s3)
# different element
s4 = s1.symmetric_difference(s2)
print(s4)

# for dis means that is all element must different
s1.isdisjoint(s2) #it return bool value
# issuperset means all value of s2 lies in s1 then it called true

