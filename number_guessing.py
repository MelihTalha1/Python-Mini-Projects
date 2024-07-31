import random

top_of_range=input("Type a number: ")

if top_of_range.isdigit(): # The isdigit() method returns True if all the characters are digits, otherwise False.
    top_of_range=int(top_of_range)

    if top_of_range <=0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()        

#r=random.randrange(-5,11)  #between-5 and 10 
#r=random.randint(11) #include 11
random_number=random.randint(0,top_of_range)
guesses=0

while True:
    guesses+=1
    user_guess =input("Make a guess: ")
    if user_guess.isdigit(): # The isdigit() method returns True if all the characters are digits, otherwise False.
        user_guess=int(user_guess)
    else:
        print("Please type a number next time.")
        continue  

    if user_guess ==random_number:
        print("You got it!")
        break
    
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")    

print("You got it in",guesses,"guesses") # we dont't need a space ,automatically add spacesin between them.We dont need convert int.
