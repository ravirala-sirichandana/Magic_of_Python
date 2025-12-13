weight=float(input('Enter your weight :'))
unit=input('Enter kilos or pounds as (k or p) :' )
if unit=='k':
    weight *= 2.205
    unit='Lbs'
    print(f'your weight is {round(weight,2)}{unit}')
elif unit=='p':
    weight /= 2.205
    unit='Kgs'
    print(f'your weight is {round(weight,2)}{unit}')
else:
    print(f'{unit} was not valid')

    
