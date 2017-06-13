from django.shortcuts import render

# Create your views here.


def home(request):
    """
    Renders the landing page
    :param request:
    :return:
    """
    return render(request, 'home.html')
