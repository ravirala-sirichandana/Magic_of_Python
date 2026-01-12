temp=float(input('Enter the temperature  : '))
unit=input('Enter the unit of temperature as(C OR F): ')
if unit=='C':
    temp=round((9*temp)/(5+32),1)
    print(f' The temperature in Farenheit is : {temp}Farenheit ')
elif unit=='F':
    temp=round((temp-32)*(5/9),1)
    print(f' The temperature in Celcius is : {temp} Celcius')
else:
    print(f'{unit} is invalid unit')