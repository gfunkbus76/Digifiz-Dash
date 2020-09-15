def print_lol(items):
	for item in items:
		if isinstance(item,list):
			print_lol(item)
		else:
			print(item)

