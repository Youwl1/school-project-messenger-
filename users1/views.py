from django.shortcuts import redirect, render
from django.contrib import auth
from .forms import  ProfileForm, UserLoginForm, UserRegistrationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("home"))
    else:
        form = UserLoginForm

    context: dict[str, any] = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse("chat"))
    else:
        form = UserRegistrationForm
    context: dict[str, str] = {
        'title': 'Home - Регистрация',
        'form': form,
    }
    return render(request, 'users/registration.html', context)

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль обновлен")
            return HttpResponseRedirect(reverse("profile"))
    else:
        form = ProfileForm(instance=request.user)
    context: dict[str, str] = {
        'title': 'Home - Кабинет',
        'form': form,
        'user': user,
    }
    return render(request, 'users/profile.html', context)
@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('registration'))
