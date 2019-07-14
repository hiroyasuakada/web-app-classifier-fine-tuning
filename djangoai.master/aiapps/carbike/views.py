from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import PhotoForm
from .models import Photo


def index(request):
    template = loader.get_template('carbike/index.html')
    context = {'form': PhotoForm()}
    return HttpResponse(template.render(context, request))


def predict(request):
    if not request.method == 'POST':
        return
        redirect('carbike:index')

    form = PhotoForm(request.POST, request.FILES)
    if not form.is_valid():
        raise ValueError('Formが不正です')

    photo = Photo(image=form.cleaned_data['image'])
    predicted, percentage = photo.predict()

    template = loader.get_template('carbike/result.html')

    context = {
        'photo_name': photo.image.name,
        'photo_data': photo.image_src(),
        'predicted': predicted,
        'percentage': percentage,
    }

    return HttpResponse(template.render(context, request))

