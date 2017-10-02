from django.shortcuts import render


def get_index(request):
    return render(request, 'blogposts.html')


def get_about(request):
    return render(request, 'about.html')


def get_contact(request):
    return render(request, 'contact.html')


def get_payment(request):
    return render(request, 'payment.html')
