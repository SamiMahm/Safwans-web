from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method=="POST":
        contact=Contact()
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        Subject=request.POST.get('Subject')
        contact.Name=Name
        contact.Email=Email
        contact.Subject=Subject
        contact.save()
        return render(request, 'redirect.html')
    return render(request, 'index.html')