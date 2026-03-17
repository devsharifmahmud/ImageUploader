from django.shortcuts import render
from .forms import ImageForm

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')