from pylab import *
x=[]
y=[]
for i in range(20):
    x.append(i)
    y.append(7-(3*i))
print(x)
print(y)
plot(x,y,'o-')
show()
