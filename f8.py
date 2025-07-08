import numpy
from scipy import stats

speed=[99,86,87,88,111,86,103,]

u=stats.mode(speed)
print(u)
y=sorted(speed)
print(y)
f=numpy.median(speed)
print(f)
x=numpy.mean(speed)
print(x)