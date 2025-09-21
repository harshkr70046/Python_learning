print("Radhe Radhe")
name  = "Krishna"
#normal printing
print(name)
#slicing of string using forowrd and backword index
print(name[0:5])
print(name[-3:-1])
#for length
print(len(name))
#for upper case and lower case
print(name.upper())
print(name.lower())
print(name.rsplit("n"))
print(name.capitalize())
print(name.center(50))
print(len(name.center(50)))
print(name.count("a"))
print(name.endswith("na"))
print(name.endswith("h",3,5))
print("Alpha and apnum checking")
str1 = "Harshkumar"
print(str1.isalnum())
print(str1.isalpha())
str2 = "harsh001"
print(str2.isalnum())
print(str2.isalpha())
