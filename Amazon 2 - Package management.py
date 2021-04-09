def funct(dict, size, name, cap):
    if len(dict[size]['Package']) < cap:
        dict[size]['Package'].append(name)
    else:
        print("Not enough space to add your item")


dict = {"S": {"Package": ["A"]}, "M": {"Package": ["B"]}, "L": {"Package": ["C"]}}
cap = 10

size = "M"
name = "Z"
funct(dict, size, name, cap)
funct(dict, size, name, cap)
funct(dict, size, name, cap)
funct(dict, size, name, cap)
funct(dict, size, name, cap)
funct(dict, size, name, cap)
funct(dict, size, name, cap)
funct(dict, size, name, cap)
funct(dict, size, name, cap)
funct(dict, size, name, cap)

print(dict)
