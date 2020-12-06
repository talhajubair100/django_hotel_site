from django.shortcuts import render
from .models import About
# Create your views here.

def about_us(request):
    about = About.objects.last()
    templates = 'about/about.html'
    context = {
        'about': about
    }

    return render(request, templates, context)