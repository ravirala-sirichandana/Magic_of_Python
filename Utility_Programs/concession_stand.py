menu={'pizza'   :50.00,
      'popcorn' :60.00,
      'fries'   :20.50,
      'chips'   :10.00,
      'soda'    :30.00,
      'lemonade':40.50 }
print('_____________MENU___________________')
for i,j in menu.items():
    print(f'{i:10}: ${j:.2f}')
print('_____________________________________')

cart=[]
price=0
while 1:
     x=input('Enter your food item(q to quit): ')
     if x.lower()=='q':
         break
     elif menu.get(x) is not None:  #elif x in menu:     
         cart.append(x)
print('_____________YOUR CART_______________')
for i in cart:
   print(i,end='  ')
   price+=menu.get(i)
   print(menu.get(i)) # menu[i]
print(f'Your Total price is: ${price:.2f}')
print()
print('THANK YOU FOR ORDERING !😊')
print('ENJOY YOUR SNACKS 😋  AND HAVE A GEAT DAY😃')
print('_____________________________________')

