from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            first_name = user.first_name
            return render(request, 'user/profile.html', {'fname' : first_name})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('user/user-login')
    return render(request, 'user/user-login.html')


def check_user(request):
    return HttpResponse('<h1>This is Check_user</h1>')

def user_signup(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname

        myuser.save()

        messages.success(request, "Your Account has been successfully created!")
        return redirect('user/user-login')

    return render(request, 'user/user-signup.html')

def validate_user(request):
    return render(request, 'validate_user.html')