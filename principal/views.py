from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

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

def edit_page(request):
  return render(request, 'dashboard/edit-page.html')