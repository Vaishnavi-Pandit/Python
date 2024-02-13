# bar graph with ids, salaries
import matplotlib.pyplot as plt
import pandas as pd
# take employee data as a dictionary
empdata = {"empid": [1001, 1002, 1003, 1004, 1005, 1006],
"ename": ["Ganesh Rao", "Anil Kumar", "Gaurav Gupta", "Hema Chandra",
"Laxmi Prasanna", "Anant Nag"],
"sal": [10000, 23000.50, 18000.33, 16500.50, 12000.75, 9999.99],
"doj": ["10-10-2000", "3-20-2002", "3-3-2002", "9-10-2000", "10-8-2000", "9-9-1999"]}
# create a data frame
df=pd.DataFrame(empdata)
print(df)
x=df['empid']
y=df['sal']
plt.bar(x,y,color="green")
plt.show()
plt.barh(x,y,color="green")
plt.show()
