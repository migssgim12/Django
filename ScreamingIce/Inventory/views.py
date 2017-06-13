from django.shortcuts import render
from .models import Ice_Cream


# Create your views here.
def scream_maker(request):
    """
    Creates a new Ice cream record in the datagase
    from the user's submitted form data.
    A view is a function that takes an HTTP request
    and returns an HTTP response.
    :param request:
    :return:
    """

    return render(request, 'index.html')


def scream_taker(request, pk):
    """
    Retrieve the Ice cream record in the datagase
    from the user's submitted form data.
    A view is a function that takes an HTTP request
    and returns an HTTP response.
    """
    icecream = IceCream.objects.get(pk=pk)

    context = {'scream': icecream}

    return render(request, 'index.html', context)