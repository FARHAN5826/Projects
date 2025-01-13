import random

computer=random.choice([-1,0,1])
'''
stone =0
paper =1
scissore =-1
'''

youstr=input("Stone ,Paper ,Scissor ? \n");
youdic={"Stone" : 0,"Paper" : 1,"Scissor" : -1}
revdic ={0 :"Stone",1 :"Paper",-1 :"Scissor"}
you=youdic[youstr]
pcstr=revdic[computer]

print(f"You Chose {youstr} and Pc chose {pcstr}")

if(you==computer):
    print("It is Draw")
    
else :
    if(you==0 and computer==1):
        print("You Lose")
    elif(you==0 and computer==-1):
        print("You Won")
    elif(you==1 and computer==-1):
        print("You Lose")
    elif(you==1 and computer==0):
        print("You Won")
    elif(you==-1 and computer==0):
        print("You Lose")
    elif(you==-1 and computer==1):
        print("You Won")
    else:
        print("Something Went Wrong")


print("Thanks for Playing With Me (PC)")