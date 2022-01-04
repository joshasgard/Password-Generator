from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):

    try:    
        characters = list()

        if request.GET.get('uppercase'):
            characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        
        if request.GET.get('lowercase'):
            characters.extend(list('abcefghijklmnopqrstuvwxyz'))    

        if request.GET.get('special'):
            characters.extend(list('~!@#$%^&*()_+="\/|?><.:;'))
        
        if request.GET.get('numbers'):
            characters.extend(list('0123456789'))

        length = int(request.GET.get('length', 14))

        thepassword = ''
        
        for x in range(length):
            thepassword += random.choice(characters)
    except:
        thepassword = 'ERROR: Select an option to generate password'


    return render(request, 'generator/password.html', {'password': thepassword})

def about(request): 

    return render(request, 'generator/about.html')


# Use templates to display html pages instead

