import random
drawOc = "It's a Draw!"
winOc = "You won the game!"
loseOc = "You lost the game"
choicelist = ["stone", "paper", "scissors"]
userInp = int(input("for stone enter 1, for paper : 2, for scissors : 3\n"))
userChoice = choicelist[userInp-1]
compChoice = random.choice(choicelist)
outcomeDict = {"stone":{"stone":drawOc, "paper":winOc, "scissors":loseOc},
               "paper":{"stone":loseOc, "paper":drawOc, "scissors":winOc},
               "scissors": {"stone":winOc, "paper":loseOc, "scissors":drawOc}}
print(outcomeDict[compChoice][userChoice], "The computer chose : ",compChoice)

