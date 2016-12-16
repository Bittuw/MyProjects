from django.shortcuts import render
from django.views.generic import ListView
# from my_app.models import Consert
from my_app.Script import Consert, Connection

# class ConsertList(ListView):
	# model = Consert


def consert_list(request):
	con = Connection("Lab", "1234", "Lab6", "localhost")
	consert = Consert(con)
	return render(request, 'my_app/consert_list.html', {'conserts': consert.get_conserts(con)})