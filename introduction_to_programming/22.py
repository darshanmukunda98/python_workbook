from math import sqrt
s1,s2,s3 = int(input('Enter the 1st side')),int(input('Enter the 2nd side')),int(input('Enter the 3rd side'))
s=(s1+s2+s3)/2
area=sqrt(s*(s-s1)*(s-s2)*(s-s2))
print('The area of the triangle %.2f'%area)

