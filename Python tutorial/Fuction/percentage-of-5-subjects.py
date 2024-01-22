#Write a function that receives marks of a student in 5 subjects and returns the percentage of marks
def percentage(lst):
    s=sum(lst)
    n=len(lst)
    avg=sum/len(lst)
    return sum,avg

'''lst=[]
n=int(input('Enter no of elements:'))
for i in range(0,n):
  ele=int(input())
  lst.append(ele)
print(lst)'''
n=[int(i) for i in input('Enter marks in 5 subjects: ').split(',')]
print(percentage(n))
