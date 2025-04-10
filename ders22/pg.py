table = [['', '', '',],
['', '', '',],
['', '', '',]]

while True:
	while True:
		x_row = int(input("X-i hansı row-a yazmaq istəyirsən? "))
		x_column = int(input("X-i hansı column-a yazmaq istəyirsən? "))
		if table[x_row][x_column] == '':
			table[x_row][x_column] = 'x'
			break
		else:
			print("Bu xana doludur, basqa yer sec")
	print(table)
	if table[0][0] == table[0][1] == table[0][2] and table[0][0] != '':
		print(f"Winner: {table[0][0]}")
		break
	elif table[0][0] == table[1][0] == table[2][0] and table[0][0] != '':
		print(f"Winner: {table[0][0]}")
		break
	elif table[1][0] == table[1][1] == table[1][2] and table[1][0] != '':
		print(f"Winner: {table[1][0]}")
		break
	elif table[2][0] == table[2][1] == table[2][2] and table[2][0] != '':
		print(f"Winner: {table[2][0]}")
		break
	elif table[0][1] == table[1][1] == table[2][1] and table[0][1] != '':
		print(f"Winner: {table[0][1]}")
		break
	elif table[0][2] == table[1][2] == table[2][2] and table[0][2] != '':
		print(f"Winner: {table[0][2]}")
		break
	elif table[0][0] == table[1][1] == table[2][2] and table[0][0] != '':
		print(f"Winner: {table[0][0]}")
		break
	elif table[0][2] == table[1][1] == table[2][0] and table[0][2] != '':
		print(f"Winner: {table[0][2]}")
		break
	elif '' not in table[0] and '' not in table[1] and '' not in table[2]:
		print("Oyun beraberedir")
		break
	else:
		while True:
			o_row = int(input("O-u hansı row-a yazmaq istəyirsən? "))
			o_column = int(input("O-u hansı column-a yazmaq istəyirsən? "))
			if table[o_row][o_column] == '':
				table[o_row][o_column] = 'o'
				break
			else:
				print("Bu xana doludur, basqa yer sec")
		print(table)
		if table[0][0] == table[0][1] == table[0][2] and table[0][0] != '':
			print(f"Winner: {table[0][0]}")
			break
		elif table[0][0] == table[1][0] == table[2][0] and table[0][0] != '':
			print(f"Winner: {table[0][0]}")
			break
		elif table[1][0] == table[1][1] == table[1][2] and table[1][0] != '':
			print(f"Winner: {table[1][0]}")
			break
		elif table[2][0] == table[2][1] == table[2][2] and table[2][0] != '':
			print(f"Winner: {table[2][0]}")
			break
		elif table[0][1] == table[1][1] == table[2][1] and table[0][1] != '':
			print(f"Winner: {table[0][1]}")
			break
		elif table[0][2] == table[1][2] == table[2][2] and table[0][2] != '':
			print(f"Winner: {table[0][2]}")
			break
		elif table[0][0] == table[1][1] == table[2][2] and table[0][0] != '':
			print(f"Winner: {table[0][0]}")
			break
		elif table[0][2] == table[1][1] == table[2][0] and table[0][2] != '':
			print(f"Winner: {table[0][2]}")
			break
		elif '' not in table[0] and '' not in table[1] and '' not in table[2]:
			print("Oyun beraberedir")
			break