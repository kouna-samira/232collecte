from django.http import HttpResponse
from django.shortcuts import render, redirect

from feedback.forms import ReponseForm
from feedback.models import Feedback


# Create your views here.
def accueil(request):
    return render(request, 'accueil.html')
def collecte(request):
    if request.method == 'POST':
        form = ReponseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('merci')
    else:
        form = ReponseForm()
    return render(request, 'home.html', {'form': form})

def merci(request):
    return render(request, 'merci.html')   # ou HttpResponse("Merci")

def home(request):
    return redirect('collecte')   # ou supprime cette vue si inutile