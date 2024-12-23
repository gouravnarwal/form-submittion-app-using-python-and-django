from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages

def index(request):  #The request object represents the HTTP request that the user makes to the server. It contains information about the request, including any data submitted via forms.
    if request.method == "POST":
        form = ApplicationForm(request.POST)  #request.POST is a dictionary-like object in Django that contains all the data sent from the client (the user's browser) when they submit the form via an HTTP POST request.
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(first_name=first_name,last_name=last_name,
                                email=email,date=date,occupation=occupation)
            messages.success(request,"Form submitted successfully")
            return redirect(index)

    return render(request,"index.html")

def about(request):
    return render(request,"about.html")
