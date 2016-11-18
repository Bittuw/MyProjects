from django.shortcuts import render
from django.views.generic import View

class OrdersView(View):
	def get(self, request):
		data = {
			'orders': [
				{'title':'Первый заказ', 'id':1},
				{'title':'Второй заказ', 'id':2},
				{'title':'Третий заказ', 'id':3}
			]
		}
		return render(request, 'my_app\orders.html', data)
		
		
class OrderView(View):
	def get(self, request, id):
		data = {
			'order': {
				'id':id
			}
		}
		return render(request, "my_app\order.html", data)