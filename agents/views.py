from django.shortcuts import render
from .models import Agent

# Create your views here.

def agents_list(request):
    agents_list = Agent.objects.all()
    templates = 'agents/agents.html'
    context = {
        'agents_list': agents_list
    }

    return render(request, templates, context)