from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
#from .models import author,category,article
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from .models import registeruser
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='/login/')
def home(request):
    return render(request,'home.html')

def user_login(request):

      # if request.user.is_authenticated:
      # return render(request, 'thankyou.html')
      # else:
      forms = registeruser()

      if request.method == 'POST':
          username = request.POST.get('users')
          password = request.POST.get('pass')
          user2 = authenticate(request, username=username, password=password)
          if user2:
              # user is not None:
              login(request, user2)  # user2 ta sucessful hole login korbo
              # return render(request, 'thankyou.html') #login hole ekta page e niya jabe
              return redirect('home')
          else:
              return HttpResponse("Username or password incorrect")
      return render(request, 'log1/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
    #return render(request, 'log1/thankyou2.html')
    #return HttpResponseRedirect(login.get_absolute_url())
'''
def user_signup(request):
    if request.method == "POST":
        form =registeruser(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
        #messages.sucess(request, 'Registration sucessfully')
            return render(request,'thankyou3.html')

    else:
        form = registeruser()
    return render(request, 'signup.html',{'signup_form':form})
'''


def user_signup(request):
    if request.method == "POST":
        form =registeruser(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
        messages.success(request, "User Registration Successfully")
        return redirect('signup')

    else:
        form = registeruser()
    context = {'signup_form': form}

    return render(request, 'signup.html', context)