temp = int(input('Enter the temp '))
vel = int(input('Enter the vel '))
wci = 13.12 + 0.6215 * temp - 11.37 * (vel**0.16) + 0.3965 * temp * (vel**0.16)
print (wci)
