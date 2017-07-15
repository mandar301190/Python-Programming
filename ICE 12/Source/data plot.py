from numpy import arange,array,ones,linalg
from pylab import plot,show

xi = arange(0,9)
A = array([ xi, ones(9)])

y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]
w = linalg.lstsq(A.T,y)[0]

line = w[0]*xi+w[1]
plot(xi,line,'r-',xi,y,'o')
show()