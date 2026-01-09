import random


number_to_guess=random.randint(1,100)
while True:
    try:
        guess=int(input("guess a number between 1 and 100:  "))
        if guess < number_to_guess:
            print("too low! ")
        elif guess>number_to_guess:
            print("too high! ")
        else:
            print("congrats! you guessed my number!")
            break
    except ValueError:
        print("please Enter a valid number? ")




