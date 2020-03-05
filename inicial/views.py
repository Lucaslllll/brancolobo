from django.shortcuts import render
from .models import Doubt, Client

def index(request):
	doubts = Doubt.objects.all()
	clients = Client.objects.all()
	data = {'doubts': doubts, 'clients':clients}
	return render(request, 'index.html', data)