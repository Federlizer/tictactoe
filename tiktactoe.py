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
	for x in cell_data.keys():
		print(x)	
	
	border = "+---+---+---+\n"
	cell_column_one = "| " + cell_data[1] + " | " + cell_data[2] + " " + template + cell_data[3] + " |\n"

	total = border + cell_column_one + border

	print(total)

def check_cells():
	pass

def something_that_changes_the_data_in_():
	pass

draw_grid()
