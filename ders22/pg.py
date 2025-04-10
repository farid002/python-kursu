table = [
	['', '', '',],
	['', '', '',],
	['', '', '',]
]

def print_table(table):
	for row in table:
		print("\t".join(row))

def place_letter_and_check_winner(table, letter):
	while True:
		row = int(input(f"{letter}-i hansı row-a yazmaq istəyirsən? "))
		column = int(input(f"{letter}-i hansi column-a yazmaq istəyirsən? "))
		if table[row][column] == '':
			table[row][column] = letter
			break
		else:
			print("Bu xana doludur, basqa yer sec")
	print_table(table)
	if ((table[0][0] == table[0][1] == table[0][2] and table[0][0] != '') or
		(table[0][0] == table[1][0] == table[2][0] and table[0][0] != '') or
		(table[1][0] == table[1][1] == table[1][2] and table[1][0] != '') or
		(table[2][0] == table[2][1] == table[2][2] and table[2][0] != '') or
		(table[0][1] == table[1][1] == table[2][1] and table[0][1] != '') or
		(table[0][2] == table[1][2] == table[2][2] and table[0][2] != '') or
		(table[0][0] == table[1][1] == table[2][2] and table[0][0] != '') or
		(table[0][2] == table[1][1] == table[2][0] and table[0][2] != '')
	):
		return table, letter
	elif '' not in table[0] and '' not in table[1] and '' not in table[2]:
		return table, 'b'
	else:
		return table, ''

while True:
	table, result = place_letter_and_check_winner(table, 'x')
	if result == 'b':
		print("berabere")
		break
	elif result == 'x' or result == 'o':
		print("Winner is ", result)

	table, result = place_letter_and_check_winner(table, 'o')
	if result == 'b':
		print("berabere")
		break
	elif result == 'x' or result == 'o':
		print("Winner is ", result)