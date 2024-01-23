mylst=["apple","banana", "cherry","orange","mango","kiwi","watermelon"]
mylst[1]="guava"#replacing item at 2nd place
print(mylst)
mylst[1:3]=["blackcurrent","jamun"]#replacing item at 2nd and 3rd position.
print(mylst)
mylst[2:4]=["grapes"]#replacing items at 3 and 4 with one value only so total items will be reduced by 1. 
print(mylst)
#insert item 
#without replacing value we can insert a value.
mylst.insert(3,"chiku")
print(mylst)