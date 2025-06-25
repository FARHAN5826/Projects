import random

import pyttsx3

engine =pyttsx3.init()

computer=random.choice([-1,0,1])
'''
stone =0
paper =1
scissore =-1
'''
engine.say("Stone ,Paper ,Scissor ?")
engine.runAndWait()
youstr=input("Stone ,Paper ,Scissor ? \n")

youdic={"Stone" : 0,"Paper" : 1,"Scissor" : -1}
revdic ={0 :"Stone",1 :"Paper",-1 :"Scissor"}
you=youdic[youstr]
pcstr=revdic[computer]


engine.say(pcstr)
engine.runAndWait()

print(f"You Chose {youstr} and Pc chose {pcstr}")
engine.say(f"You Chose {youstr} and Pc chose {pcstr}")
engine.runAndWait()

if(you==computer):
    print("It is Draw")
    engine.say("It is Draw ")
    engine.runAndWait()
    
else :
    if(you==0 and computer==1):
        print("You Lose")
        engine.say("You Lose ")
        engine.runAndWait()

    elif(you==0 and computer==-1):
        print("You Won")
        engine.say("You Won ")
        engine.runAndWait()
    elif(you==1 and computer==-1):
        print("You Lose")
        engine.say("You Lose ")
        engine.runAndWait()
    elif(you==1 and computer==0):
        print("You Won")
        engine.say("You Won ")
        engine.runAndWait()
    elif(you==-1 and computer==0):
        print("You Lose")
        engine.say("You Lose ")
        engine.runAndWait()
    elif(you==-1 and computer==1):
        print("You Won")
        engine.say("You Won ")
        engine.runAndWait()
    else:
        print("Something Went Wrong")
        engine.say("Something Went Wrong")
        engine.runAndWait()

engine.say("Thanks for Playing With Me ")
engine.runAndWait()
print("Thanks for Playing With Me (PC)")
