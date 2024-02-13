# to display employees of different depts in pie chart
import matplotlib.pyplot as plt
# take the percentages of employees of 4 departments
slices = [50, 20, 15, 15]
# take the departments names
depts = ['Sales', 'Production', 'HR', 'Finance']
# take the colors for each department
cols = ['magenta', 'cyan', 'brown', 'gold']
# create a pie chart
plt.pie(slices, labels=depts, colors=cols, startangle=90, explode=(0,
0.2, 0.2, 0), shadow=True, autopct='%.2f%%' )#autopct to show the percentage
# set titles and legend
plt.title('WIPRO')
plt.show()