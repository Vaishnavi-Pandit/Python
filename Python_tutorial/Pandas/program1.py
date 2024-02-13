import pandas as pd
df = pd.read_csv("file path") # read data from csv file.

print(df)
df2 = pd.read_excel("file path","sheet name") # read data from excel file
print(df2)
df3=pd.read_table("file path",delim_whitespace=True, names=('A','B','C','D'))
print(df3)# reading data from text file
df4=pd.DataFrame(objectname in dictionary)
print(df4)#reading data from dictionary
df5=pd.DataFrame(object name in list, column=['empno','empname'])
print(df5)#reading data from list