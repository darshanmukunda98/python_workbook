mass = float(input('Enter the mass of the material '))
temp = float(input('Enter the temp change '))
eng = mass * 4.186 * temp
print('The total energy  change is %.2f '%(eng))
print('the  bill amt is %.2f'%((eng/3.6+6)*8.9))
