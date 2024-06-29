from django.shortcuts import render, redirect
from django.views import View
from .forms import UserCreateForm, LoginForm,ProfileUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin

class Register(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {'form': create_form}
        return render(request, 'register.html', context=context)
    
    def post(self, request):
        create_form = UserCreateForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect(reverse_lazy('users:login'))
        else:
            context = {
                'form': create_form
            }
            return render(request, 'login.html', context)

class Login(View):
    def get(self, request):
        login_form = LoginForm()
        context = {'form': login_form}
        return render(request, 'login.html', context=context)
    
    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            print(user)
            login(request, user)
            return redirect(reverse_lazy('home'))
        else:
            context = {'form': login_form}
        return render(request, 'login.html', context=context)
    
class Loguot(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('users:login')
    

class Profile(LoginRequiredMixin, View):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        print(user)
        context = {'user': user}
        return render(request, 'profile.html', context=context)
    

class ProfileEdit(LoginRequiredMixin, View):
    def get(self, request):
        user_update = ProfileUpdateForm(instance=request.user)
        return render(request, 'profile-edit.html', {'form': user_update})

    def post(self, request):
        user_update = ProfileUpdateForm(instance=request.user, data=request.POST, files=request.FILES)
        if user_update.is_valid():
            user_update.save()
            return redirect('users:profile')

        return render(request, 'profile.html', {"form": user_update})