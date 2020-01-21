name = "pablo"
name2="eve"
gretting = f"Hello! , {name} and {name2} "

print(gretting)

name3="franco"
name4="ana"

gretting2 = "hello {} and {}"
with_name=gretting2.format(name3,name4)
print(with_name)