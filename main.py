import string


counters = dict()
lst = list()


def enter_file():
	fname = input('Ingrese archivo: ')
	try:
		fhand = open(fname)
	except:
		print(f'El archivo "{fname}" no se puede abrir')
		exit()
	for line in fhand:
		# Create translation table
		translation_table = str.maketrans('', '', string.punctuation)
		# Apply translation using translation table
		line = line.translate(translation_table)
		line = line.lower()
		words = line.split()
		# Convert the list to a string
		words = "".join(words)
		for word in words:
			if word not in counters:
				counters[word] = 1
			else:
				counters[word] += 1


def add_letters_list():
	for k, v in list(counters.items()):
		# Agregar sólo letras
		if k.isalpha():
			lst.append((v, k))
	return lst


def sum_values():
	sum = 0
	for k, v in list(counters.items()):
		sum += v
	return sum


def sort_dictionary():
	ordered_list = lst.sort(reverse=True)
	return ordered_list


def get_percentage():
	total = sum_values()
	for v, k in lst:
		percentage = f'{(int(v) / total * 100):.1f}%'
		result = print(f'\t{k} \t{v} \t{percentage}')
	return result


def print_list():
	print('----------------------------------------------')
	print('Frecuencia y porcentaje de aparición de letras')
	print('----------------------------------------------')
	get_percentage()
	print('----------------------------------------------')
	print(f'\tTotal de letras: {len(lst)}')
	print('----------------------------------------------')


def main():
	enter_file()
	add_letters_list()
	sort_dictionary()
	print_list()


main()