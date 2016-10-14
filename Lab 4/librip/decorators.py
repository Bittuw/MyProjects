from functools import wraps

def print_result(func):
	@wraps(func)
	def result(*args, **kwargs):
		print(func.__name__)
		temp = func(*args, **kwargs)
		if isinstance(temp, list):
			print("\n".join(map(str, temp)))
		elif isinstance(temp, dict):
			print("\n".join(map(lambda x: "{} = {}".format(x[0], x[1]), temp.items())))
		else:
			print(temp)
		return temp
	return result