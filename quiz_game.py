import random

def quiz ():
    print("Welcome to my computer quiz!")

    playing = input("Do you want to play? ")

    if playing.lower() != "yes":
        quit()
    print("Okay! Let's play :")
    score = 0

    answer = input("mnhwe the goat of football? ")
    if answer.lower() ==( "cristiano" or "cr7" or "ronaldo"):
        print("7ag ba3d ")
        score += 100
    else:
        print("zri6 cr7 3ammek!")
        score -=  100

    print("natijtek= " + str(score) + " f ma3revet ballon")

def quess():
    top_of_range = input("type an number: ")
    
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)

        if top_of_range <= 0:
            print("pls type a number larger than 0 next time")
            quit()
    else:
        print("pls type a number larger than 0 next time")
        quit()
    random_number = random.randint(0, top_of_range)

    while True:
        pass