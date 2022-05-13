import pyttsx3
import random

eng = pyttsx3.init()
voice = eng.getProperty("voices")[1].id
eng.setProperty("rate", 150)
eng.setProperty("voice", voice)


def RandomGuessing(start_val, end_val):
    eng.say("Welcome to the Random Guessing Game. What is your name?")
    eng.runAndWait()

    player = input("Enter your name:")

    rnum = random.randint(start_val, end_val)

    eng.say("Hello {}. Guess a number from {} to {}.".format(player, start_val, end_val))
    eng.runAndWait()

    unum = int(input("Enter your number:"))
    guess = []

    if unum >= start_val and unum <= end_val:
        guess.append(unum)
        while unum != rnum:
            if unum < rnum:
                eng.say("Please try higher value")
                eng.runAndWait()
            else:
                eng.say("Please try lower value")
                eng.runAndWait()

            unum = int(input("Enter your number:"))
            guess.append(unum)

        else:
            if len(guess) <= 5:
                eng.say("{}, you have won the game. Congratulations.".format(player))
                eng.runAndWait()
            else:
                eng.say(
                    "{}, unfortunately you have lost. You have tried {} times. Try again".format(player, len(guess)))
                eng.runAndWait()
    else:
        eng.say("{}, Restart the game and try with a number, within {} to {}.".format(player, start_val, end_val))
        eng.runAndWait()