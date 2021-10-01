from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}

    return render(request, 'main/home.html', context)


def about(request):
    context = {}

    return render(request, 'main/about.html', context)


def faq(request):
    context = {}

    return render(request, 'main/faq.html', context)

def adminConfirm(request):
    context = {}

    return render(request, 'main/adminConfirm.html', context)