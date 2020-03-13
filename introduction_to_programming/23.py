from math import pi,tan
n = int(input('Enter the  number of sides'))
s = int(input('Enter the length of each side'))
area = ((n*s**2)/(4*tan(pi/n)))
print('The area of the polygon is %.2f'%area)
