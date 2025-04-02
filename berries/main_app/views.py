from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Berry

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def berry_index(request):
    berries = Berry.objects.all()
    return render(request, 'berries/index.html', {'berries': berries})


def berry_detail(request, berry_id):
    berry = Berry.objects.get(id=berry_id)
    return render(request, 'berries/detail.html', {'berry': berry})

class BerryCreate(CreateView):
    model = Berry
    fields = '__all__'

class BerryUpdate(UpdateView):
    model = Berry
    fields = ['variety', 'description', 'season']

class BerryDelete(DeleteView):
    model = Berry
    success_url = '/berries/'