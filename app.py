import random
x = 1
y = 100

inc = 0
while True:
    number = int(input("Guess Number: "))
    print("Your Guess is: ", number)
    inc +=1
    print("Attempts:", inc)
    total = random.randint(x, y)
    print ("Correct Number is : ",total)

    if number == total:
        print("Congratulation! You guessed it right nigga.")
        break
    elif number <= total:
        print("Too low, Try again. ")
    elif number >= total:
        print("Too high, Try Again.")


    
