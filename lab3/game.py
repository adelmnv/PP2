import random
def guess_the_num():
    count =0
    username = input("Hello! What is your name?\n")
    print(f"\nWell, {username}, I am thinking of a number between 1 and 20.")
    num = random.randint(1,20)
    guess = int(input("Take a guess.\n"))
    count+=1
    print()
    while guess != num:
        if guess > num:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
        guess = int(input("Take a guess.\n"))
        count+=1
        print()
    print(f"Good job, {username}! You guessed my number in {count} guess(es)!")
