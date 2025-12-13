operator=input('Enter an operator(e.g. +,-,*,/) : ')
number1=float(input('Enter your first number :'))
number2=float(input('Enter your second number :'))
if operator=='+' :
    print(round((number1+number2),3))
elif operator=='-' :
    print(round((number1-number2),3))
elif operator=='*' :
    print(round((number1*number2),3))
elif operator=='/' :
    print(round((number1/number2),3))
else :
    print(f'{operator} is not a valid operator')
