import pandas as pd
import matplotlib.pyplot as plt
years=['2013','2014','2016','2019']
profits=[6,7.6,10,9]
#line plot
plt.plot(years,profits,color='orange')
plt.title("Vaishnavi traders")
plt.xlabel("profits")
plt.ylabel("years")
plt.show()
#Scatter plot
plt.scatter(years,profits,color='blue')
plt.title("Vaishnavi traders")
plt.xlabel("profits")
plt.ylabel("years")
plt.show()