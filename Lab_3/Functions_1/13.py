import random
print("Hello! What is your name?")
name = str(input())
print("Well " + name + ", I am thinking of a number between 1 and 20.")
right = random.randint(0, 20)
quess = -1
cnt = 0
while quess != right:
    print("Take a guess.")
    quess = int(input())
    if quess > right:
        print("Too high")
    elif quess < right:
        print("Too low")
    cnt += 1
print("Good job,", name, "You guessed my number in", cnt, "guesses!")        