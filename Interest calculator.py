principle=float(input('Enter principle value(p): ' ))
while principle <0 :
    print("Principal should be greater than 0.")
    principle=float(input('Enter principle value(p): ' ))
rate=float(input('Enter interest rate value : ' ))
while rate <0 :
    print("Interest rate should be greater than 0.")
    rate=float(input('Enter interest rate value: ' ))
time=float(input('Enter time in years : ' ))
while time<0:
    print('Time should be graeter than zero.')
    time=float(input('Enter time in years : ' ))
total=principle*pow((1+rate/100),time)
print(f'Your Balance after {time} years is :${total:.2f}')

