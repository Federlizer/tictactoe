cell_data = {
	1: " ",
	2: " ",
	3: " ",
	4: " ",
	5: " ",
	6: " ",
	7: " ",
	8: " ",
	9: " "
}

i = 0



def draw_grid():
	border = "+---+---+---+\n"
	row1 = "| " + cell_data[1] + " | " + cell_data[2] + " | " + cell_data[3] + " |\n"
	row2 = "| " + cell_data[4] + " | " + cell_data[5] + " | " + cell_data[6] + " |\n"
	row3 = "| " + cell_data[7] + " | " + cell_data[8] + " | " + cell_data[9] + " |\n"

	print(border + row1 + border + row2 + border + row3 + border)

def check_cells(number, player):
	if (cell_data[number] == "X" or cell_data[number] == "O"):
		return False
	else:
		cell_data[number] = player
		return True
	
def check_winner():
	print("checked winner")


draw_grid()
while(True):
	if(i % 2 == 0):
		try:
			chosen_cell = int(input("X choose: "))
		except ValueError:
			print("Please type in a number!")	
			continue

		if(chosen_cell < 1 or chosen_cell > 9):
			print("Please type in a number between 1 and 9")
			continue


		if(check_cells(chosen_cell, "X")):
			draw_grid()
			check_winner()
		else:
			print("This slot has already been used, please try another one")	
			continue


	elif(not(i % 2 == 0)):
		try:
			chosen_cell = int(input("O choose: "))
		except ValueError:
			print("Please type in a number!")
			continue

		if(chosen_cell < 1 or chosen_cell > 9):
			print("Please type in a number between 1 and 9")
			continue

		if(check_cells(chosen_cell, "O")):
			draw_grid()
			check_winner()
		else:
			print("This slot has already been used, please try another one")
			continue

	i += 1
