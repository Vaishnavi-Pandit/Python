import numpy as np
def degree(n):
    d=(n*180)/np.pi
    return d
n=int(input('Enter a no: '))
print('Degree is equal to: ',degree(n))