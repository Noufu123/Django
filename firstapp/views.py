from django.shortcuts import render

# Create your views here.

def load_page(request):
    return render(request,'hello.html')