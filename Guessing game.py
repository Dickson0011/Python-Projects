import random
smaller=int(input("Enter smaller number"))
larger=int(input("Enter larger number"))
myNumber = random.randint(smaller,larger)
count = 0
while True:
    count +=1
    userNumber = int(input("Enter Your Guess"))
    if userNumber < myNumber:
        print("Tooo small")
    elif userNumber > myNumber:
        print("too large")
    else:
        print("congratulations u got it in",count,"tries")

