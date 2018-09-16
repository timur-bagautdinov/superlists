from django.shortcuts import render


def home_page(request):
    """
    home page
    :return:
    """
    return render(request, 'home.html')
