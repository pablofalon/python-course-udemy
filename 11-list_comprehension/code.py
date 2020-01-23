"""myList = ["pablo","ana","franco","eve"]"""

"""number = [1,3,5]
doubled = []

for num in number:
    doubled.append(num * 2)

print(doubled)"""

"""
number = [1,2,3]
doubled = [num * 2 for num in number]
LO QUE QUEREMOS HACER + EL FOR CON LA VARIABLE A ITERAR
print(doubled)
"""

myList = ["pablo","ana","franco","eve"]
nombresConA = [friend for friend in myList if friend.startswith("a")]
print(nombresConA)


