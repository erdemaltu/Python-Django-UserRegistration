from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout,login,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from pip._internal.locations import user_site
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from main.forms import LoginForm, SignUpForm, AccountForm
from account.models import Account

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    User = get_user_model()
    users = User.objects.all()
    account= Account.objects.all()
    count= Account.objects.all().count()
    context = {
        "users" : users,
        "account":account,
        "count":count,
        }
    return render(request,"index.html",context)

@login_required(login_url='/login/')
def userprofile_view(request,id):
    User = get_user_model()
    profile = User.objects.get(id=id)
    account= Account.objects.get(user_id=id)
    context = {
        "profile" : profile,
        "account": account,
        }
    return render(request,"user_profile.html",context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')

                else:
                    messages.info(request, 'Disable Account')
            else:
                messages.info(request, 'Check Your Username and Password')
    else:
        form=LoginForm()

    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup_view(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            current_user = request.user
            data = Account()
            data.user_id = current_user.id
            gender = form.cleaned_data.get('gender')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            data.gender = gender
            data.phone = phone
            data.address = address
            data.save()
            messages.success(request,'Account has been created')
            return HttpResponseRedirect('/')
    else:
        form = AccountForm()
        
    return render(request, 'signup.html',{'form': form})
