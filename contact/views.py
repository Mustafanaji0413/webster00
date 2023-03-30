from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from .models import Contact


@login_required
def contact_admin(request):
    # Initialize messages with a default value
    messages = Contact.objects.none()

    if request.method == 'POST':
        message_id = request.POST.get('message_id')
        status = request.POST.get(f"status_{message_id}")
        if message_id and status:
            contact = Contact.objects.filter(id=message_id).first()
            if contact:
                contact.status = status
                contact.save()

    # Retrieve all messages and order them by created_at date
    messages = Contact.objects.all().order_by('-created_at')

    # Pass the messages to the template
    return render(request, 'contact_admin.html', {'messages': messages})


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
