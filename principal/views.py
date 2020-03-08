from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from inicial.models import Doubt, Client
from .models import Product
from .forms import DoubtForm, ClientForm, ProductForm

from django.core.mail import send_mail
from django.core import mail
from django.template.loader import render_to_string
from .tokens import account_activation_token

import json

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

def do_logout(request):
  logout(request)
  return redirect('login')

def forget_password(request):
  if request.method == 'POST':
    try:
      user = User.objects.get(email=request.POST['email'])  
    except User.DoesNotExist:
      user = None
    print(request.POST['email'])
    if user != None:
      msg_html = render_to_string('dashboard/email.html', {
        'user': user,
        'token':account_activation_token.make_token(user)
      })
      connection = mail.get_connection()
      connection.open()

      email = mail.EmailMessage(
          'Suporte - RemixManiacs',
          msg_html,   
          'entrego.oficialdelivery@gmail.com', # 'from'
          [user.email,], # 'to'
          connection=connection
      )

      email.send()
      confirmEmail = True
      return render(request, 'dashboard/forget-pass.html', {'confirmEmail': confirmEmail})
    else:
      error = True
      return render(request, 'dashboard/forget-pass.html', {'error': error})
      
  else:
    return render(request, 'dashboard/forget-pass.html')

def confirme_password(request, pk, token):
  try:
    user = User.objects.get(pk=pk)  
  except User.DoesNotExist:
    user = None
  
  if user != None:
    
    if account_activation_token.check_token(user, token):
      return render(request, 'dashboard/change-password.html', {'user_status':user})
    else:
      return HttpResponse("<h1 align='center'>Token does not exist</h1></br></br><a align='center' href='login'>click here</a>")
  else:
    return HttpResponse("<h1 align='center'>User does not exist</h1></br></br><a align='center' href='forget_password'>click here</a>")


def change_password(request):
  if request.method == 'POST':
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 == password2:
      user_status = request.POST['user_status']
      
      try:
        user = User.objects.get(pk=user_status)
      except User.DoesNotExist:
        user = None
      except ValueError:
        user = None

      if user != None:
        user.set_password(password1)
        user.save()
        # auth = Auth_User.objects.get(user=user)
        # auth.delete()
        return redirect('login')
      else:
        return HttpResponse("<h1 align='center'>Please, use the link of your email</h1>")        

    else:
      error = True
      return render(request, 'dashboard/change-password.html', {'error':error})

  error = False
  return render(request, 'dashboard/change-password.html', {'error':error})

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
      return HttpResponse("<h1 align='center'>Complete the fields</h1></br></br><a align='center' href='add_client'>click here</a>")
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
      
      return HttpResponse("<h1 align='center'>Complete the fields</h1></br></br><a align='center' href='add_client'>click here</a>")
  else:
    form = ClientForm(instance=client)

  data['form'] = form; data['client'] = client;

  return render(request, 'dashboard/client/edit-client.html', data)

def delete_client(request, pk):
  client = Client.objects.get(pk=pk)
  client.delete()
  return redirect('index')


# crud client

def add_product(request):
  data = {}
  if request.method == 'POST':
    form = ProductForm(data=request.POST, files=request.FILES)
    if form.is_valid():
      form.save()
      return redirect('list_product')
    else:
      HttpResponse(json.dumps(form.errors))
  else:
    form = ProductForm()
  data['form'] = form

  return render(request, 'dashboard/product/add-product.html', data)

def list_product(request):
  data = {}
  products = Product.objects.all()
  data['products'] = products
  return render(request, 'dashboard/product/list-product.html', data)

def edit_product(request, pk):
  data = {}
  product = Product.objects.get(pk=pk)
  
  if request.method == 'POST':
    product.image.delete()
    form = ProductForm(data=request.POST, files=request.FILES, instance=product)
    if form.is_valid():
      form.save()
      return redirect('index')
    else:
      
      return HttpResponse("<h1 align='center'>Complete the fields</h1></br></br><a align='center' href='add_doubt'>click here</a>")
  else:
    form = ProductForm(instance=product)

  data['form'] = form; data['product'] = product;

  return render(request, 'dashboard/product/edit-product.html', data)

def delete_product(request, pk):
  product = Product.objects.get(pk=pk)
  product.delete()
  return redirect('index')