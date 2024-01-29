# Write a function that receives marks of a student in 5 subjects and returns the percentage of marks
def percentage(lst):
    s = sum(lst)
    n = len(lst)
    avg = s / len(lst)
    return avg, s


'''lst=[]
n=int(input('Enter no of elements:'))
for i in range(0,n):
  ele=int(input())
  lst.append(ele)
print(lst)'''
lst = [int(i) for i in input('Enter marks of 5 subject').split()]
print(len(lst))
assert 6 > len(lst) > 0, "marks of only 5 subjects are allowed."
for i in lst:
    assert 100 > i > 0, 'Invalid Marks.'
s,  y = percentage(lst)
print('percentage=%f/n sum=%d' % (s, y))
print("percentage and sum are respectively ", percentage(lst))
