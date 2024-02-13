#append items
mylst=["apple","banana", "cherry","orange","mango","kiwi","watermelon"]
mylst.append("orange")#value will be inserted at last.
print(mylst)
mylst.insert(1,"blackcurrent")#item will be inserted at position 1.
#extende list
trop=["java","python","c"]
mylst.extend(trop)
print(mylst)
#you can add any literable object using extend() method in the list literable means tuple, set, dictionary.
my=("kuku","mukku","jadu")
mylst.extend(my)
print(mylst)