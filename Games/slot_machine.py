#python slot machine
import random
def spin():
    symbols=['🍒','🍋','🍉','🔔','⭐']
    return [random.choice(symbols) for i in range(3)]

def print_row(row):
    print('**************')
    print(' | '.join(row))
    print('**************')
def payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍒':
            return bet * 3
        elif row[0]=='🍋':
            return bet * 4
        elif row[0]=='🍉':
            return bet * 5
        elif row[0]=='🔔':
            return bet * 10
        elif row[0]=='⭐':
            return bet * 20
    return 0   

        
def main():
    balance=100
    print('*************************')
    print('WELCOME TO PYTHON SLOTS')
    print('SYMBOLS : 🍒 🍋 🍉 🔔 ⭐ ')
    print('*************************')
    while balance>0:
        print(f'your current balance is : ${balance}')
        bet=input('Place your bet amount: ')
        if not bet.isdigit():
            print('Please enter a valid number')
            continue
        bet=int(bet)
        if bet>balance:
            print('Insufficient bet')
            continue
        if bet<=0:
            print('Bet must be greater than zero')
            continue
        balance-= bet
        row=spin()
        print('SPINNING .....\n')
        print_row(row)

        pay=payout(row,bet)
        if pay>0:
            print(f'YOU WON ${pay} ☺️☺️☺️')
        else:
            print(f'SORRY YOU LOST THIS ROUND  😔😔')
        
        balance+=pay
        print('*******************************************')
        play_again=input('DO YOU WANT TO SPIN AGAIN? (Y/N): ').upper()
        print('*******************************************')
        if play_again=='N':
            break
    
    print(f'GAME IS OVER !!!! YOUR FINAL BALANCE IS ${balance} \nTHANKS FOR PLAYING 😊😊😊')
    print('*******************************************')
if __name__ == '__main__':
     main()

