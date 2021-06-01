from random import randint
lst = []
user_number = 0
Greet = input()
print("Hey there! Lets play a little guessing game.")
print("Guess a number between 0 and 25")
def game():
    rand_number = randint (0,25)
    i = 1
    r = 1
    while i < 8:
        user_number = int(input("Enter Guess: "))
        lst.append(int(user_number))
        if user_number < rand_number:
            print ("Nope, Its greater than that")
            print ("You have " + str(8 - i) + " guesses left!")
        elif user_number > rand_number:
            print ("Nope, Its less than that")
            print ("You have " + str(8-i) + " guesses left!")
        elif user_number == rand_number:
            print ("Damn. You win!")
            print ("The number was indeed " + str(rand_number))
            r = 0;
            break
        else: 
            print("You have " + str(8-1) + " guesses left!")
            continue
        i = i+1
    if r==1: 
        print ("AHHAHA YOU LOOSE!")
        print ("The number was " + str(rand_number) + " you fool")
game()
print("Your guess log: ")
print(lst)
