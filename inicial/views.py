from django.shortcuts import render
from .models import Doubt, Client, PhotoProdutoAfterBefore
from principal.models import Initial
from principal.models import Product

def index(request):
	doubts = Doubt.objects.all()
	clients = Client.objects.all()
	Photo_Product = PhotoProdutoAfterBefore.objects.all()
	products = Product.objects.all()
	initial = Initial.objects.get(pk=1)
	data = {'doubts': doubts, 'clients':clients, 'Photo_Product':Photo_Product,
	 		'products': products, 'initial': initial}
	return render(request, 'index.html', data)
