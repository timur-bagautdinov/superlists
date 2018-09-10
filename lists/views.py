from django.http import HttpResponse


def home_page(request):
    """
    home page
    :return: http response
    """
    return HttpResponse('<html><title>To-Do lists</title></html>')
