from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# from django.http import HttpResponse
# Create your views here.
def index(request):
 #context is a set of varibles
    context = {
        "variable1": "this is sent",
        "variable2": "Deepali is great"
    }
    
    return render(request, 'index.html')
    # return HttpResponse("Hello, world. You're at the home page.")
 
def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from home.models import Contact

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc', '')  # Set default value to empty string if desc is not provided
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()  # Call the save method to save the Contact object to the database
        messages.success(request, "Your message has been sent.")
        # Redirect to the contact page to prevent form resubmission
        return redirect('contact')

    # Pass messages to the template context
    context = {'messages': messages.get_messages(request)}
    return render(request, 'contact.html', context)

