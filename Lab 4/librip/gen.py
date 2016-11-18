from random import randint


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
	assert len(args) > 0, "Not specified search parameter!"
	assert isinstance(items, list), "The function accepts only list!"
	for item in items:
		assert isinstance(item, dict), " d"
		if len(args)==1:
			if item[args[0]] is not None:
				yield item[args[0]]
		else:
			temp = {key:item[key] for key in args if item[key] is not None}
			yield temp
		
    # Необходимо реализовать генератор 


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
	for x in range(num_count):
		yield randint(begin, end)
    # Необходимо реализовать генератор
