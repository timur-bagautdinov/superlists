from django.shortcuts import render
from django.shortcuts import HttpResponse


def home_page(request):
    """
    home page
    :return:
    """
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })
