from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages


def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_msgs')
        else:
            messages.add_message(request, messages.INFO, "Login failed")
            return redirect ('frontpage')
    return render(request, 'useraccounts/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('frontpage')

def user_register(request):
    if request.method == "POST":
        user = User()
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.username = request.POST.get('username')
        #Checks if username exits 
        if User.objects.filter(username=user.username).exists():
            messages.add_message(request, messages.INFO, "Username already exists.")
            return redirect('frontpage')
        user.email = request.POST.get('email')
        #Checks if email exits    
        if User.objects.filter(email=user.email).exists():
            messages.add_message(request, messages.INFO,"Email already exists.")
            return redirect('frontpage')
        user.set_password(request.POST.get('password'))
        user.save()
        messages.add_message(request, messages.INFO, "You registered successfully.")
    return redirect('frontpage')   

def edit_profile(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.email = request.POST.get('email')
        #Checks if email exits    
        if User.objects.filter(email=user.email).exists():
            messages.add_message(request, messages.INFO,"Email already exists.")
            return redirect('edit_profile')
        user.save(update_fields=['first_name', 'last_name', 'email'])
        messages.add_message(request, messages.INFO, "Edited profile successfully.")
    return render(request, 'useraccounts/edit_profile.html') 