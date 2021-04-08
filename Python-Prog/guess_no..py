#guess the number

guess = 9
while guess > 0:
    x = int(input("Enter a number\n"))
    if x > 18:
        print("Enter a smaller number")
    elif x < 18:
        print("Enter a larger number")
    else:
        print("You guessed it right!!")
        print("No.of attempts = ", 10-guess)
        break
    guess = guess - 1
    print("No. of guesses left = ", guess)

if guess == 0:
    print("you lost")