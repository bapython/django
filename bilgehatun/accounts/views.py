from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def register(request):
    if request.method == 'POST':
        email       = request.POST['email']
        username    = request.POST['username']
        last_name   = request.POST['last_name']
        password1   = request.POST['password1']
        password2   = request.POST['password2']
        first_name  = request.POST['first_name']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                # print('Username taken!')
                messages.info(request,'Username taken!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                # print('Email taken!')
                messages.info(request,'Email taken!')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username = username, password = password1, email = email, first_name = first_name, last_name = last_name)
                user.save()
                print('user created')
                return redirect('login') # login sayfası tasarlandıktan sonra eklenecek.
        else:
            # print("Password not matching..")
            messages.info(request,'Password not matching..')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'accounts/register.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')




def logout(request):
    auth.logout(request)
    return redirect('/')