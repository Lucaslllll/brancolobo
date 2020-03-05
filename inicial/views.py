from django.shortcuts import render
from .models import Doubt, Client, PhotoProdutoAfterBefore

def index(request):
	doubts = Doubt.objects.all()
	clients = Client.objects.all()
	Photo_Product = PhotoProdutoAfterBefore.objects.all()
	data = {'doubts': doubts, 'clients':clients, 'Photo_Product':Photo_Product}
	return render(request, 'index.html', data)