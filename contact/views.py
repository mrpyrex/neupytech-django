from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import get_template
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['message']
            subject = 'Contact Received'
            message = '%s %s' %(comment, name)
            emailFrom = form.cleaned_data['sender']
            emailTo = [settings.EMAIL_HOST_USER]
            send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        
            # saving contact form data to dbase

            new_contact = Contact(name=request.POST['name'], sender=request.POST['sender'], phone=request.POST['phone'], message=request.POST['message'])
            new_contact.save()
            return redirect('contact:contact')         

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
    