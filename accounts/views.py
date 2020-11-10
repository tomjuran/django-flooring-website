from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login as dj_login


from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.

from .models import *
from .forms import OrderForm, CreateUserForm
#from .decorators import unauthenticated_user, allowed_users, admin_only


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

        return redirect('login')
            
    context = {'form':form}
    return render(request, 'accounts/register.html', context)


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            dj_login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username Or password incorrect')    

    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'accounts/dashboard.html')


#def products(request):
    #return render(request, 'accounts/products.html')


def about(request):
    return render(request, 'accounts/about.html')


def customer(request):
    return render(request, 'accounts/customer.html')

def vinyl(request):
    return render(request, 'accounts/vinyl.html')

def laminate(request):
    return render(request, 'accounts/laminate.html')

@login_required(login_url='login')
def sales(request):
    return render(request, 'accounts/sales.html')



