from math import radians, sin, cos, acos
t1,g1 = radians(float(input('Enter 1st lat'))),radians(float(input('Enter 1st long')))
t2,g2 = radians(float(input('Enter 2st lat'))),radians(float(input('Enter 2st long')))
d = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(abs(g1-g2)))
print('The distance between two points of earth %.2fkm  '%d)
