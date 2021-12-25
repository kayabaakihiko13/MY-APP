import random 
x=[]
while True:
    print(10*"="+"The Roll(not Rick :V) of Dices"+10*"=")
    n=int(input("How many want the dice to play"))
    for a in range(0,2):
        a=random.randrange(1,6)
        x.append(a)
    print(x)
    if x[0]==x[n-1]:
        print("The Element is same")
    else:
        print("Oke")
    print("You want to play again (Y/N):")
    input()
    if "Y" or "y":
        x.clear()
        continue
    else:
        break