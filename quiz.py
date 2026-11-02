print("Welcome to the Networking Quiz!")
print("Answer 3 questions and earn 1 point for each correct answer.")
score = 0

print("Question 1: Which device connects different networks?")
print("A. Switch")
print("B. Switch")
answer = input("Enter A or B: ")

if answer == "B":
    print("Correct!")
    score += 1
else:
    print("The correct answer is B. Router.")

print("Question 2: What does DNS do?")
print("A. Translates domain names into IP addresses")
print("B. Supplies power to network devices")
answer = input("Enter A or B: ")

if answer == "A":
    print("Correct!")
    score += 1
else:
    print("The correct answer is A. Translates domain names into IP addresses.")


print("Question 3: Which command tests whether a device replies over a network?")
print("A. mkdir")
print("B. ping")
answer = input("Enter A or B: ")

if answer == "B":
    print("Correct!")
    score += 1
else:
    print("The correct answer is B. ping.")

print("Your final score:", score, "out of 3")
