from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .models import MyUser
from .forms import UserRegisterForm, UserLoginForm


def user_sign_up_view(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('index')

        else:
            print(form.errors)
    form = UserRegisterForm()

    return render(request, 'app/sign_up.html', {'form': form})


def user_login_view(request):

    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            user_email = form.cleaned_data['email']
            user_password = form.cleaned_data['password']

            user = authenticate(request, username=user_email, password=user_password)

            if user:
                login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()

    return render(request, 'app/login.html', {'form': form})


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('index')
