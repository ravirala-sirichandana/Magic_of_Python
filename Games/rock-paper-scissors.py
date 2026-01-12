import random
options=('rock','paper','scissors')
run=True
while run:
    player=None
    c=random.choice(options)
    while player not in options:
        player=input('Enter a choice (rock,paper,scissors) : ')
    print(f'player : {player}')
    print(f'computer : {c}')
    if player==c:
        print('ITS A TIE')
    elif player=='paper' and c=='rock':
        print('YOU WIN THE GAME!!!')
    elif player=='rock' and c=='scissors':
        print('YOU WIN THE GAME!!!')
    elif player=='scissors' and c=='paper':
        print('YOU WIN THE GAME!!!')
    else:
        print('YOU LOSE!')
    choice = input('WANT TO PLAY AGAIN ? (y/n) : ').lower()
    if choice != 'y':
        run = False
print('THANKS FOR PLAYING!!!☺️')

 
