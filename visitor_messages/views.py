from django.shortcuts import render

# Create your views here.


def contact_view(request):
    form = None

    context = {'form': form}

    return render(request, 'visitor_messages/contact.html',context)