ques=('1.What comes down but never goes up?',
   '2.Which animal can sleep standing up?',
   '3.Which animal is known for laughing?',
   '4.Which animal is famously known for sleeping the most?',
   '5.What is the largest egg on Earth?')

option=('A. Rain  B. Age  C. Stairs  D. Temperature',
   'A.Dog  B.Cow  C.Horse  D.Cat',
   'A. Monkey  B. Hyena  C. Dog  D. Dolphin',
   'A. Dog  B. Cat  C. Sloth  D. Horse',
   'A. Ostrich  B. Crow C. Eagle  D. Penguin')
ans=('B','C','B','C','A')
guess=[]
incr=0
s=0
for i in ques:
    print('_________________________________________________')
    print(i)
    print(option[incr])
    x=input('Enter your option :').upper()
    guess.append(x)
    if x==ans[incr]:
        s+=1
        print('CORRECT OPTION :)')
    else:
        print('INCORRECT OPTION !!!!')
        print(f'{ans[incr]}  IS THE CORRECT OPTION ')
    incr+=1
s=int((s/len(ques))*100)
print('_________________________________________________')
print('--------------------RESULTS ---------------------')
print(f'Guesses : ',*guess)  
print(f'Answers : ',*ans) 
print(f'Score   :   {s}%')
print('-------------------------------------------------')