p = float(input('Enter the pressure '))
v = float(input('Enter the volume '))
r = 8.314
t = float(input('Enter the temp '))
print('the amount of material in moles %.2f'%((p*v)/(r*(t+273))))
