from tkinter import *
#create tkinter instance
import random as rd
start=0
x=[]
while True:
    print(10*"="+"Dice play"+10*"=")
    print(10*"="+"Let's Play"+10*"=")
    print("how many you want :")
    n=int(input())
    for i in range(0,n):
        i=rd.randrange(1,6)
        x.append(i)

    print(x)
    if x[0]==x[n-1]:
        print("the Value same")
    else:
        print("oke")
    print("You want play again")
    input()
    if n=="Y" or "y":
        x.clear()
        continue
    else:
        break