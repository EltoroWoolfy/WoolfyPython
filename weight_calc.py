weight = input('your weight is? ')
type = input('is it kg or pounds? ')
if type == 'pounds':
    print('your weight in kg ' + str(float(int(weight)) * 0.45))
elif type ==  'kg':
    print('your weight in pounds ' + str(float(int(weight)) * 2.20))
