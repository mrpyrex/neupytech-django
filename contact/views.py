from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

# Create your views here.


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'Contact Received'
            comment = '%s %s' %(message, name)
            try:
                send_mail(subject, comment, from_email, ['neupytechng@gmail.com'], fail_silently=False)
                new_contact = Contact(name=request.POST['name'], from_email=request.POST['email'], phone=request.POST['phone'], message=request.POST['message'])
                new_contact.save()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact:success')
    context = {
        'title': 'Contact Us',
        'form': form
        }
    return render(request, "contact/contact.html", context)

def successView(request):
    context = {
        'title': 'Success!',
    }
    return render(request, 'contact/success.html', context)
