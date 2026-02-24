#python banking system

def Balance(balance):
    print('----------------------')
    print(f'YOUR BALANCE IS ${balance:.2f}')

def deposit():
    print('----------------------')
    amount=int(input('ENTER AN AMOUNT TO BE DEPOSITED : '))
    
    if amount<=0:
        print('----------------------')
        print('ITS NOT A VALID AMOUNT 🤔')
        return 0
    else:
        return amount


def withdraw(balance):
    print('----------------------')
    amount=float(input('ENTER AN AMOUNT TO BE WITHDRAWN : '))
    
    if amount> balance:
        print('----------------------')
        print('INSUFFICIENT MONEY😞')
        return 0
    elif amount<=0:
        print('----------------------')
        print('AMOUNT MUST BE GREATER THAN 0 🤨')
        return 0
    else:
        return amount

def main():    
    balance =0
    running=True
    while running:

        print('----------------------')
        print('BANKING PROGRAM')
        print('----------------------')
        print('1.Show Balance')
        print('2.Deposit')
        print('3.Withdraw')
        print('4.Exit')
        print('----------------------')
        ch=input('Enter your choice(1-4) : ')

        if ch=='1':
            Balance(balance)
        elif ch=='2':
            balance += deposit()
        elif ch=='3':
            balance -= withdraw(balance)
        elif ch=='4':
            running=False
        else:
            print('----------------------')
            print('THIS IS NOT A VALID OPTION')
            print('----------------------')
    print('----------------------')
    print('THANK YOU 😊  HAVE A NICE DAY 😊😊 !!!')
    print('----------------------')
if __name__ == '__main__' :
    main()

        














  