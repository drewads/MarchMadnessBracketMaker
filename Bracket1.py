from random import *
round = 32
teams = list(range(1, 17))
finalFour = list(range(1, 5))

print()
print("This script randomly picks a bracket (and final score) weighted by rankings.")
print()
print("Bracket groups go clockwise from top left.")
print("For that reason, it is best to fill this out on a computer.")

#bracket groups go clockwise from top left
for i in range(0,4):
	print()
	print("Section ", i + 1)
	round = 32
	teams = list(range(1, 17))
	for k in range(0,4):	
		print("Round of", round*2)
		round = int(round/2)
		teams = teams[0:round]
		for j in range(0, int(round/2)):
			if random() > ((teams[j])/(teams[j]+teams[len(teams)-1-j]))+.03:
				print(teams[j], "wins")
			else:
				print(teams[len(teams)-1-j], "wins")
				teams[j] = teams[len(teams)-1-j]

			if round == 2:
				finalFour[i] = teams[j]	

# Bracket groups go clockwise from top left
print()
print("Final Four")
round = 8
teams = finalFour
for k in range(0,2):	
	if k == 1:
		print()
		print("Finals")

	round = int(round/2)
	teams = teams[0:round]
	for j in range(0, int(round/2)):
		if random() > ((teams[j])/(teams[j]+teams[len(teams)-1-j])):
			if teams[j] != teams[len(teams)-1-j]:
				print(teams[j], "wins")
			else:
				print(teams[j], "a wins")	
		else:
			if teams[j] != teams[len(teams)-1-j]:
				print(teams[len(teams)-1-j], "wins")
			else:
				print(teams[len(teams)-1-j], "b wins")	
			
			teams[j] = teams[len(teams)-1-j]

print()
#Final Score
print("Final Score")	
middleScore = 85.7	#Median of 2018 top 10 team PPG
middleDef = 62		#Near median of 2018 top 10 team points allowed per game
score1 = randint(middleDef, int(middleScore))
score2 = randint(middleDef, int(middleScore))
if score1 > score2:
	print("Winner score:", score1)
	print("Loser score:", score2)
else:
	print("Winner score:", score2)
	print("Loser score:", score1)
