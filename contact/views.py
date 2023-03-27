from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from .models import Contact

@login_required
def contact_admin(request):
    if request.method == 'POST':
        message_id = request.POST.get('message_id')
        status = request.POST.get('status')
        if message_id and status:
            contact = Contact.objects.filter(id=message_id).first()
            if contact:
                contact.status = status
                contact.save()
    messages = Contact.objects.all().order_by('-created_at')
    status_filter = request.GET.get('status_filter', 'unread')
    if status_filter == 'read':
        messages = messages.filter(status='read')
    elif status_filter == 'handled':
        messages = messages.filter(status='handled')
    else:
        messages = messages.filter(status='unread')
    return render(request, 'contact_admin.html', {'messages': messages, 'status_filter': status_filter})
    

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, email, [settings.DEFAULT_FROM_EMAIL])
            Contact.objects.create(name=name, email=email, subject=subject, message=message)
            return render(request, 'success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def contact_success(request):
    return render(request, 'contact_success.html')