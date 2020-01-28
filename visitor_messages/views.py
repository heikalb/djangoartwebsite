from django.shortcuts import render
from .models import VisitorMessage
# Create your views here.


def contact_view(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            new_message = VisitorMessage.objects.create(**form.cleaned_data)
            form = ContactForm()


    context = {'form': form}

    return render(request, 'visitor_messages/contact.html',context)