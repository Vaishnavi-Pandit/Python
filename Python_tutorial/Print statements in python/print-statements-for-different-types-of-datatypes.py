id=60
name='shrinu'
sal=45356.8079
print('Id=',id)#to print id value.
print('Name=',name)#to print name value.
print('id=',id,"sal=",sal)
print("Name=%s,Id=%d,Sal=%f"%(name,id,sal))
print("Name=%s,Id=%5d,Sal=%.2f"%(name,id,sal))#%5d is used to add 5 spaces before the exact value and .2f is added to shot the value upto two integers after point.
print("Name=%s,Id=%5d,Sal=%10.2f"%(name,id,sal))#10.2f here 10 is used to add spaces before the value before point but the no before point will beplaced in no of spaces from right hand side before point.
print('Id={},Name={},sal={}'.format(id,name,sal))
print('Id={0},Name={2},Sal={2}'.format(id,name,sal))
print('id={:5d},name={:10s},sal={:8f}'.format(id,name,sal))#here the spaces are added before in int and float but in string spaces are added after the string.