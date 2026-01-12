import random
low=1
high=100
guess=0
ans=random.randint(low,high)
print('PYTHON NUMBER GUESSING GAME')
print(f'select a number between {low} and {high}')
run=True
while run:
    g=input('Enter your guess : ')
    if g.isdigit():
        g=int(g)
        guess+=1
        if (g<low or g>high):
            print('That number is out of range !!!')
            print(f'Please select a number between {low} and {high}')
        elif (g>ans):
            print('That number is too high')
        elif (g<ans):
            print('That number is too low')
        else:
            print('CORRECT NUMBER !!! ')
            print(f'The answer was {ans}')
            print(f'Number of guesses are : {guess}')
            print('SEE YOU NEXT TIME 👋\nHAVE A GOOD DAY ☺️')
            run=False
    else:
        print('INVALID GUESS')
        print(f'Please select a number between {low} and {high}')
