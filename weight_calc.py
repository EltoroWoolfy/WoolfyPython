weight = float(int(input('your weight is? ')))
type = input('is it kg or pounds? ')
if type == 'pounds':
    converted = weight * 0.45
    print('your weight in kg ' + str(converted))
elif type ==  'kg':
    converted = weight * 2.20
    print('your weight in pounds ' + str(converted))
