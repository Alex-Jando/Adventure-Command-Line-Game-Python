import random

userName = input("Enter Your Username: ")

difficulty = ""

correctDifficulty = False

areas = ["Cave", "Forest", "Ravine", "Castle", "Town", "Deep Dark Place"]

enemies = ["Goblin", "Dragon", "Witch", "Creeper", "Jake Pauler"]

options = """OPTIONS:
"s" To Search
"a" To Attack
"f" To Flee
"l" To Leave A Trap
"""

life = 0

def search():

	global life

	find = random.randint(0, 20)

	if find == 7 or find == 10 or find == 11 or find == 12 or find == 13 or find == 14 or find == 15 or find == 16 or find == 17 or find == 18 or find == 19 or find == 20:
		print("You Didn't Find Anything\n")
	elif find == 1 or find == 2 or find == 3 or find == 4 or find == 5 or find == 6 or find == 8 or find == 9:
		attack()
	elif find == 0:
		print("You Got Ligma And Died!")
		life = 0


def attack():
	global life

	find = random.randint(0,1)

	if find == 0:
		battleOn = False
		print("\nYou Failed To Find An Enemy\n")

	elif find == 1:
		battleOn = True

		random.shuffle(enemies)

		enemy = enemies[0]

		print(f"You Encountered A {enemy}\n")

	while battleOn == True:
		
		damage = random.randint(0,1)

		if damage == 1:

			life -= damage
			if life < 0:
				break
			print(f"You Fought Hard And Took {damage} Damage\n")
			print(f"Your You Now Have {life} Life")

			validInput = False

			while validInput == False:
				choice = input("OPTIONS:\n\"a\" To Keep Attacking\n\"f\" To Flee:\n\nChoose An Option: ")
				if choice == "a":
					validInput = True
				elif choice == "f":
					validInput = True
					battleOn = False
					flee()
				else:
					validInput = False

		elif damage == 0:
			print(f"You Defeated The {enemy} Congragulations!")
			battleOn = False
			life += 1
			print(f"\nPlus One Life, You Now Have {life} Life\n")
		

def flee():
	print("\nYou Ran Hard And Found A New Location:\n")

def leaveATrap():
	global life

	target = random.randint(0,15)

	random.shuffle(enemies)

	enemy = enemies[0]

	if target == 0 or target == 1 or target == 2 or target == 3 or target == 4 or target == 5 or target == 6 or target == 7 or target == 8 or target == 9:
		print(f"You Killed A {enemy}!")
		life = random.randint(1,5)
		if life == 5:
			print(f"Wow, You Got +1 Life. Now You Have {life} Life")

	elif target == 10 or target == 11 or target == 12 or target == 13 or target == 14:
		print("\nYou Didn't Kill Anything\n")

	elif target == 15:
		print("You Killed An Inocent Villager. Then The Villagers Executed You, It Was A Slow And Painful Death!")
		life = 0



def decideOnChoice(choice):

	if choice == "s":
		search()
	elif choice == "a":
		attack()
	elif choice == "f":
		flee()
	elif choice == "l":
		leaveATrap()
	else:
		return "falseChoice"

def game():
	global life

	life = lifeStandard

	while life > 0:

		random.shuffle(areas)

		area = areas[0]

		print(f"The User {userName} Has Stumbled Upon A {area}: \n")
		print(options)

		choice = input("Choose An Option: ")

		decideOnChoice(choice)

while correctDifficulty == False:

	difficulty = input("Enter The Desired Difficulty (\"Easy\", \"Medium\", \"Hard\"): ")

	if difficulty.lower() == "easy":
		correctDifficulty = True
		difficulty = 0
		lifeStandard = 5

	elif difficulty.lower() == "medium":
			correctDifficulty = True
			difficulty = 1
			lifeStandard = 4

	elif difficulty.lower() == "hard":
			correctDifficulty = True
			difficulty = 2
			lifeStandard = 3
	else:
		correctDifficulty = False


game()

while True:


	print("You Died Press Enter To Play Again Or E To Exit: ")
	choice = input()

	if choice == "":
		game()
	elif choice.lower() == "e":
		break
	else:
		break
