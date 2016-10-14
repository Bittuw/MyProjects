# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
# Пример использования
# with timer():
#   sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно 5.5
 
import time


class timer:
	@staticmethod
	def get_time():
		return time.time()
	def __enter__(self):
		self.time_start = __class__.get_time()
	def __exit__(self, exc_type, exc_temp, exc_tb):
		print(__class__.get_time() - self.time_start)