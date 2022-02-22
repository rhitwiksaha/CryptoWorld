from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print("in the index function")
    return render(request, 'index.html')

def creator(request):
    print("in the creator function")
    return render(request, 'creator.html')
