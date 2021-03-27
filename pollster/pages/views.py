from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.forms import inlineformset_factory
from .decorators import unauthenticated_user


@login_required(login_url='login')
def index(request):
  return render(request, 'pages/index.html')


 # Registration page
@unauthenticated_user
def registerPage(request):

      form = CreateUserForm()
      if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
          form.save()
          user = form.cleaned_data.get('username')
          messages.success(request, 'Account was created for ' + user)
          return redirect('login')
		
      context = {'form':form}
      return render(request, 'pages/register.html', context)


@unauthenticated_user
def loginPage(request):
  if request.method == "POST":
    username = request.POST.get('username') 
    password = request.POST.get('password')

    user = authenticate(request, username=username,password=password)
    if user is not None:
      login(request,user)
      return redirect('index')
    else:
      messages.info(request, "Username or Password Not so good...")
  context = {}
  return render(request, 'pages/login.html', context)

def logoutUser(request):
  logout(request)
  return redirect('login')


def view_profile(request):
  context = {
    'user': request.user
  }
  return render(request, 'pages/profile.html', context)