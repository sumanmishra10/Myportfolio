from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/home.html')


def contact(request):
    return render(request, 'portfolio/contact.html')




