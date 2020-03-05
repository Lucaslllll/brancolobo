from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from inicial.models import Doubt, Client
from .forms import DoubtForm, ClientForm

@login_required(login_url='login')
def index(request):
  return render(request, 'dashboard/dashboard.html')

def verifify_user(email, password):
  try:
    user = User.objects.get(email=email)
  except User.DoesNotExist:
    user = None
    
  if user is not None:
    user = authenticate(username=user.username, password=password)
    return user
  else:
    return user

def do_login(request):
  
  if request.method == 'POST':
    email = request.POST['email']; 
    password = request.POST['password'];
    user = verifify_user(email, password) 
        
    if user is not None:
      login(request, user)
      return redirect('index')
    else:
      error = True
      return render(request, 'dashboard/login.html', {'error': error})

  return render(request, 'dashboard/login.html')

def forget_password(request):
  pass

# client doubt

def add_doubt(request):
  data = {}
  if request.method == 'POST':
    form = DoubtForm(data=request.POST, files=request.FILES)
    if form.is_valid():
      form.save()
      return redirect('list_doubt')
    else:
      return HttpResponse("<h1 align='center'>Complete the fields</h1></br></br><a align='center' href='add_doubt'>click here</a>")
  else:
    form = DoubtForm()
  data['form'] = form
  return render(request, 'dashboard/doubt/add-doubt.html', data)

def list_doubt(request):
  data = {}
  doubts = Doubt.objects.all()
  data['doubts'] = doubts
  return render(request, 'dashboard/doubt/list-doubt.html', data)

def edit_doubt(request, pk):
  data = {}
  doubt = Doubt.objects.get(pk=pk)
  
  if request.method == 'POST':
    form = DoubtForm(data=request.POST, instance=doubt)
    if form.is_valid():
      form.save()
      
      return redirect('index')
    else:
      
      return HttpResponse("<h1 align='center'>Complete the fields</h1></br></br><a align='center' href='add_doubt'>click here</a>")
  else:
    form = DoubtForm(instance=doubt)

  data['form'] = form; data['doubt'] = doubt;

  return render(request, 'dashboard/doubt/edit-doubt.html', data)

def delete_doubt(request, pk):
  doubt = Doubt.objects.get(pk=pk)
  doubt.delete()
  return redirect('index')


# crud client

def add_client(request):
  data = {}
  if request.method == 'POST':
    form = ClientForm(data=request.POST, files=request.FILES)
    if form.is_valid():
      form.save()
      return redirect('list_client')
    else:
      return HttpResponse("<h1 align='center'>Complete the fields</h1></br></br><a align='center' href='add_doubt'>click here</a>")
  else:
    form = ClientForm()
  data['form'] = form

  return render(request, 'dashboard/client/add-client.html', data)

def list_client(request):
  data = {}
  clients = Client.objects.all()
  data['clients'] = clients
  return render(request, 'dashboard/client/list-client.html', data)

def edit_client(request, pk):
  data = {}
  client = Client.objects.get(pk=pk)
  
  if request.method == 'POST':
    form = ClientForm(data=request.POST, instance=client)
    if form.is_valid():
      form.save()
      
      return redirect('index')
    else:
      
      return HttpResponse("<h1 align='center'>Complete the fields</h1></br></br><a align='center' href='add_doubt'>click here</a>")
  else:
    form = ClientForm(instance=client)

  data['form'] = form; data['client'] = client;

  return render(request, 'dashboard/client/edit-client.html', data)

def delete_client(request, pk):
  client = Client.objects.get(pk=pk)
  client.delete()
  return redirect('index')
