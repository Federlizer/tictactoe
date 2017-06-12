cell_data = {
	1: "X",
	2: " ",
	3: "O",
	4: " ",
	5: " ",
	6: " ",
	7: " ",
	8: " ",
	9: " "
}




def draw_grid():
	border = "+---+---+---+\n"
	row1 = "| " + cell_data[1] + " | " + cell_data[2] + " | " + cell_data[3] + " |\n"
	row2 = "| " + cell_data[4] + " | " + cell_data[5] + " | " + cell_data[6] + " |\n"
	row3 = "| " + cell_data[7] + " | " + cell_data[8] + " | " + cell_data[9] + " |\n"
	print(border + row1 + border + row2 + border + row3 + border)





def check_cells():
	pass

def something_that_changes_the_data_in_():
	pass

draw_grid()
