from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, MakeUserAccount, UserQuoteForm
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponse
from django.conf import settings



def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")


@login_required
def logout(request):
    """A view that logs the user out and redirects back to the home page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('home'))


def login(request):
    """A view that manages the login form"""
    if request.user.is_authenticated:	
        return redirect(reverse('home'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['user_password'])
        messages.error(request, "You have successfully logged in")

        if user:
            auth.login(user=user, request=request) 
            return redirect(reverse('home'))
        else:
            login_form.add_error(None, "Your username and/or password are incorrect")
    else:
        login_form = UserLoginForm()

    return render(request, 'login.html', {'login_form': login_form})


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})


def quote(request):
    """A view that displays the quote page for the user"""
    return render(request, 'quote.html')


def email(request, emailto):
    """ function for sending a quote to a email """
    if request.method == 'POST':
        send_mail(request.user.email, ['testingdev1990@gmail.com'], fail_silently=False)
    return HttpResponse('%s' % email)


def register(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = MakeUserAccount(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = MakeUserAccount()
    return render(request, 'register.html', {
        "registration_form": registration_form})
