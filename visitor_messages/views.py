from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# Create your views here.


def contact_view(request):
    form = ContactForm(request.POST or None)
    success_msg = ''

    if form.is_valid():
        form.save()

        message = 'Name: {0}\n\nEmail: {1}\n\nMessage:\n\n{2}'

        message = message.format(form.cleaned_data['name'],
                                 form.cleaned_data['email'],
                                 form.cleaned_data['message'])

        send_mail('New message on your art website (Django version)',
                  message,
                  settings.EMAIL_HOST_USER,
                  ['heikal93@gmail.com'],
                  fail_silently=False)

        form = ContactForm()
        success_msg = 'Thank you for your message'

    context = {'form': form, 'success_msg': success_msg}

    return render(request, 'visitor_messages/contact.html', context)
