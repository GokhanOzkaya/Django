from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"index.html")

def furnitures(request):
    return render(request,"furnitures.html")

def testimonial(request):
    return render(request,"testimonial.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")