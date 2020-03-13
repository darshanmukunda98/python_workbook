spd = 86400
sph = 3600
spm = 60
sec = int(input('Enter the number of seconds'))
days = sec / spd
sec = sec % spd
h =sec / sph
sec = sec % spd
m = sec / spm
sec = sec % spm
print('The equivalent duration is %d:%02d:%02d:%02d ' %(days,h,m,sec))
