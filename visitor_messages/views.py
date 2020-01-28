from django.shortcuts import render
from .forms import ContactForm
# Create your views here.


def contact_view(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ContactForm()

    context = {'form': form}

    return render(request, 'visitor_messages/contact.html', context)
