import random
upper_bound = 25
lower_bound = 0
tobe_guess = random.randint(lower_bound, upper_bound)
guess = 0
while guess != tobe_guess:
    guess = int(input("Enter guess: "))
    if guess > 0:
        if guess > tobe_guess:
            print ("Too large")
        elif guess < tobe_guess:
            print ("Too small")
        else:
            
        
