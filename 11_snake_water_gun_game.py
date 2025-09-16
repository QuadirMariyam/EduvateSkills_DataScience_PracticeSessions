import random


computer = random.choice([1, 0, -1])
gameDict = {1: 'Snake', 0: 'Water', -1: 'Gun'}
youstr = input("Enter a Choice among s, w and g: ")
youDict = {'s': 1, 'w': 0, 'g': -1}
you = youDict[youstr]

print(f"Your Choice: {gameDict[you]}\nComputer's Choice: {gameDict[computer]}")

if you == computer:
    print("Draw")

elif (computer == -1 and you == 0) or (computer == 0 and you == 1) or (computer == 1 and you == -1):
    print("You win :)")

else:
    print("You lose :(")
