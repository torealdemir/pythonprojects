print("welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Lets play!!")
score = 0

answer = input("What does Cpu stand for? ")
if answer.lower() == "central processing unit":
    print("Coorect!")
    score += 1
    print(score)
else:
    print("Incorrect!")

answer = input("What does gpu stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
    print(score)
else:
    print("Incorrect!")

answer = input("What does ram stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
    print(score)
else:
    print("Incorrect")

answer = input("What does psu stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
    print(score)
else:
    print("Incorrect")


print("You got " + str(score) + "questions correct!")
