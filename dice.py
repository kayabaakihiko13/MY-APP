import random 
import os
value=list()
start =True
while start==True:
    print('your want to join the the role:')
    input_1=input()
    if input_1 in 'yY':
        for a in range(0,2):
            a=random.randrange(1,14)
            value.append(a)
        print(value)
        print('print you want to play again')
        input_2=input()
        if input_2 in 'yY':
            value.clear()
            os.system('cls')# tergantung Operasi system
            continue
        else:
            print('thank you')
            break

    else:
        print('Thank your time,keep well ')
        break