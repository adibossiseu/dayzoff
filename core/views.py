from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('core:index'))
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})


#@login_required(login_url=reverse('core:login'))
def index(request):
    return render(request, 'core/index.html')


class LoginView(BaseLoginView):

    template_name = 'core/login.html'
