import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .forms import ContactForm
from .models import Contact

# login view checks entered username and password against database and
# either logs you in or return error if something went wrong
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

# django logout function

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    form = RegisterForm()
    page = 'register'

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    context = {'page': page, 'form': form}
    return render(request, 'base/login_register.html', context)

def home(request):
    name = str(request.user)

    if request.user.is_authenticated:
        form = ContactForm()
        contact_list = Contact.objects.order_by('created')
        if request.method == 'POST':
            form = ContactForm(request.POST, request.FILES)
            if form.is_valid():
                contact = form.save(commit=False)
                contact.owner = request.user
                contact.save()
                return redirect('home')
            else:
                messages.error(request, 'An error occurred during contact creation')
        context = {'form': form, 'contacts' : contact_list, 'name': name}
        return render(request, 'base/home.html', context)
    else:
        return redirect('login')

def contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    content = {'contact': contact}
    return render(request, 'base/contact.html', content)

def delete(request, contact_id):
    object = get_object_or_404(Contact, pk=contact_id)
    object.ProfilePicture.delete()
    object.delete()
    return redirect('home')


def settings(request):

    return render(request, 'base/settings.html')