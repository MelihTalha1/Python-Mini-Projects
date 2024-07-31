print("Welcome to the quiz game!")

play=input("Do you want to play? ")

if play.lower() != "yes":
    quit() #this will just immediately terminate the program

print("Okay! Let's play :)")
score=0

answer=input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")    


answer=input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")       


answer=input("What does RAM stand for? ").lower() #answer is already converted to do lower 
if answer == "random access memory":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")         



answer=input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")        

print("You got "+str(score)+" questions correct!")   
print("You got "+str((score/4)*100) +"%.")     