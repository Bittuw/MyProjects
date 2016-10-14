# Итератор для удаления дубликатов
class Unique(object):
	def __init__(self, items, **kwargs):
		self.ignore_case = kwargs.get('ignore_case') is not None and kwargs.get('ignore_case')
		self.items = iter(items)
		self.seen = set()

	def __next__(self):
		while True:
			temp = self.items.__next__()
			temp_val = str(temp).lower() if self.ignore_case else temp
			if temp_val not in self.seen:
				self.seen.add(temp_val)
				return temp
	def __iter__(self):
		return self
