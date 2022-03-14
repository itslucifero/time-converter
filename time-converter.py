
print('TIME CONVERTER BY YAHIA OUALI')
days = int(input('Please enter days : '))
hours = int(input('Please enter hours : '))
minutes = int(input('Please enter minutes : '))


daysinsec = int(24 * 60 * days)
hoursinsec = int(60 * hours)
mininsec = int(60 * minutes)

res = int((daysinsec + hoursinsec ) * 60 + mininsec)
result = print( f'time converted to seconds is : ' , res , 'seconds')
