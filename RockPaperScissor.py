print("Rock...")
print("Paper...")
print("Scissor...")
import random


players_move = input("Player,play your move:")
random_num = random.randint(0,2)

if random_num == 0:
	computers_move = "Rock"
elif random_num == 1:
	computers_move = "Paper"
else:
	computers_move ="Scissor"
print(f"Computer plays {computers_move}")

if players_move == computers_move:
	print("Draw")
elif players_move == "Rock":
	if computers_move == "Paper":
		print("Computer wins")
	else:
		print("Player wins")
elif players_move == "Paper":
	if computers_move == "Rock":
		print("Player wins")
	else:
		print("Computer wins")
elif players_move == "Scissor":
	if computers_move =="Rock":
		print("Computer wins")
	else:
		print("Player wins")
else:
	print("Something went wrong")		
	 





	






