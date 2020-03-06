from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm, UserQuoteForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.conf import settings


def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")


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

            if user:
                auth.login(user=user, request=request)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('home'))
            else:
                login_form.add_error(None, "Your username and/or password are incorrect")
    else:
        login_form = UserLoginForm()

    return render(request, 'login.html', {'login_form': login_form})


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    return render(request, 'profile.html')


def quote(request):
    """A view that displays the quote page for the user"""
    return render(request, 'quote.html')
    name = request.POST.get('UserQuoteForm.full_name', '')
    quote = request.POST.get('UserQuoteForm.user_quote', '')
    details = request.POST.get('phone_number', 'date')
    if request.method == 'POST' and name and quote and details:
        quote(request.user.email, ['testingdev1990@gmail.com'], fail_silently=False)
    return render(request, 'home')


def register(request):
    """A view that manages the registration form"""
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('home'))

            else:
                messages.error(request, "Unable to register you in at this time!")
    else:
        registration_form = UserRegistrationForm()

    return render(request, 'register.html')
