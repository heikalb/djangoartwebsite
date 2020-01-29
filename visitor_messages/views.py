from django.shortcuts import render
from .forms import ContactForm
# Create your views here.


def contact_view(request):
    form = ContactForm(request.POST or None)
    success_msg = ''

    if form.is_valid():
        form.save()
        form = ContactForm()
        success_msg = 'Thank you for your message'

    context = {'form': form, 'success_msg': success_msg}

    return render(request, 'visitor_messages/contact.html', context)
