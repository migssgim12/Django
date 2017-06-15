from django.shortcuts import render, redirect
from .models import Media, Tag
from .forms import MediaModelForm

# Create your views here.

def create(request):
    """

    :param request:
    :return:
    """
    if request.method == "GET":
        form = MediaModelForm()

    elif request.method == "POST":
        form = MediaModelForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('/gallery/list')

    # form = MediaModelForm()
    context = {'form':form}
    return render(request, 'create.html', context)

def retrieve(request, pk):
    """

    :param request:
    :return:
    """
    media = Media.objects.get(id=pk)
    context = {'media': media}
    return render(request, '', context)

def update(request, pk):
    """


    :param request:
    :return:
    """
    media = Media.objects.get(id=pk)

    if request.method == "GET":
        form = MediaModelForm(instance=media)

    elif request.method == "POST":
        form = MediaModelForm(instance=media, data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('/gallery/display')

    # form = MediaModelForm()
    context = {'form':form}
    return render(request, 'create.html', context)

def delete(request, pk):
    """

    :param request:
    :return:
    """
    media = Media.objects.get(id=pk)
    message = 'Deleted Media #{}'.format(media.id)
    media.delete()
    context = {'status': message}
    return render(request, '', context)

def display(request):
    """

    :param request:
    :return:
    """

    context = {}
    return render(request, '', context)