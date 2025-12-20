#shopping cart
foods=[]
prices=[]
total=0
while True:
    x=input('Enter a food item(q to quit): ')
    if x.lower() =='q':
        break
    else:
        
        p=float(input(f'Enter price of {x}: '))
        foods.append(x)
        prices.append(p)
print('-------------Your Cart------------')
for i in foods:
    print(i,end=' ')
print()
for x in prices:
    total+=p
print(f'Your total price is ${total}')