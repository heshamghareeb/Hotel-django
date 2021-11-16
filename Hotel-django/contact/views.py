from django.shortcuts import redirect, render
from .models import ContactDetails
from .forms import ContactForm
from django.core.mail import BadHeaderError
from django.core.mail import send_mail as sm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def send_mail(request):
    contactdetails = ContactDetails.objects.last()
    template = 'contact/contact.html'
    
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid:
            subject = request.POST.get('subject', '')
            print(type(subject))
            from_email = request.POST.get('from_email', '')
            print(type(from_email))
            message = request.POST.get('message', '')
            print(type(message))
            
            try:
                sm(subject,message,from_email, ['test@gmail.com'])
            except BadHeaderError:
                return HttpResponse('invalid header')
            return redirect('contact:success')
    else:
        contact_form = ContactForm()
    
    context = {
        'contactdetails' : contactdetails  , 
        'contact_form' : contact_form,
    }

    return render(request, template , context)


def success(request):
    return HttpResponse('Message Sent Successfully')