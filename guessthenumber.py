import random
import pyttsx3

engine = pyttsx3.init()

number = random.randint(1, 25)

while True:
    engine.say("Guess the number (between 1 and 25): ")
    engine.runAndWait()
    guess = int(input("Guess the number (between 1 and 25): "))
    if guess == number:
        print("Bingo, You guessed right!")
        engine.say("Bingo, You guessed right!")
        engine.runAndWait()
        break
    elif guess < number:
        print("Too low! Try again.")
        engine.say("Too low! Try again.")
        engine.runAndWait()
    else:
        print("Too high! Try again.")
        engine.say("Too high! Try again.")
        engine.runAndWait()