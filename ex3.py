print("Lets play a game, you will have to guess the number in my mind and you will get total 9 guesses ")
num = 18
guess = 9
usernum = 0
while(guess > 0):
    usernum = int(input("Enter your guessed number"))
    if usernum < 18 and usernum >15:
        print("your number is slightly less than the original the number")
        guess = guess-1
        print("number of guesses left = ", guess)
        continue
    elif usernum <= 15 and usernum >5:
        print("your number is less than the original the number")
        guess = guess - 1
        print("number of guesses left = ", guess)
        continue
    elif usernum <= 5:
        print("your number is very less than the original the number")
        guess = guess - 1
        print("number of guesses left = ", guess)
        continue
    elif usernum > 18 and usernum < 21:
        print("your number is slightly greater than the original the number")
        guess = guess - 1
        print("number of guesses left = ", guess)
        continue
    elif usernum >=21 and usernum<=25:
        print("your number is greater than the original the number")
        guess = guess - 1
        print("number of guesses left = ", guess)
        continue
    elif usernum >= 25:
        print("your number is much greater than the original the number")
        guess = guess - 1
        print("number of guesses left = ", guess)
        continue
    elif usernum == num:
        guess = guess - 1
        print("congratulations, you guessed the correct answer in ", 9-guess, "guesses")
        break
if guess == 0 :
    print("You lose! Try again")

