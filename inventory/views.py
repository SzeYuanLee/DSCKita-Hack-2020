from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import *

from .forms import *


def index(request):
    return render(request, 'inv/index.html')


def  dashboard(request):
    return render(request,'inv/dashboard.html')


def display_facemasks(request):
    items = FaceMasks.objects.all()
    context = {
        'items': items,
        'header': 'FaceMasks',
    }
    return render(request, 'inv/index.html', context)


def display_sanitizers(request):
    items = Sanitizers.objects.all()
    context = {
        'items': items,
        'header': 'Sanitizers',
    }
    return render(request, 'inv/index.html', context)


def display_faceshields(request):
    items = FaceShields.objects.all()
    context = {
        'items': items,
        'header': 'Mobiles',
    }
    return render(request, 'inv/index.html', context)


def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'inv/add_new.html', {'form': form})


def add_facemask(request):
    return add_item(request, FaceMaskForm)


def add_sanitizer(request):
    return add_item(request, SanitizerForm)


def add_faceshield(request):
    return add_item(request, FaceShieldForm)


def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'inv/edit_item.html', {'form': form})


def edit_facemask(request, pk):
    return edit_item(request, pk, FaceMasks, FaceMaskForm)


def edit_sanitizer(request, pk):
    return edit_item(request, pk, Sanitizers, SanitizerForm)


def edit_faceshield(request, pk):
    return edit_item(request, pk, FaceShields, FaceShieldForm)


def delete_facemask(request, pk):
    template = 'inv/index.html'
    FaceMasks.objects.filter(id=pk).delete()

    items = FaceMasks.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_sanitizer(request, pk):
    template = 'inv/index.html'
    Sanitizers.objects.filter(id=pk).delete()

    items = Sanitizers.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_faceshield(request, pk):
    template = 'inv/index.html'
    FaceShields.objects.filter(id=pk).delete()

    items = FaceShields.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)
