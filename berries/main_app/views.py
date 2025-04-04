from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Berry
from .forms import PickingForm

# Create your views here.

# function-based views


class Home(LoginView):
    template_name = 'home.html'


def about(request):
    return render(request, 'about.html')


def berry_index(request):
    berries = Berry.objects.all()
    return render(request, 'berries/index.html', {'berries': berries})


def berry_detail(request, berry_id):
    berry = Berry.objects.get(id=berry_id)
    picking_form = PickingForm()
    return render(request, 'berries/detail.html', {
        'berry': berry,
        'picking_form': picking_form
    })


# class-based views
class BerryCreate(CreateView):
    model = Berry
    fields = '__all__'


class BerryUpdate(UpdateView):
    model = Berry
    fields = ['variety', 'description', 'season']


class BerryDelete(DeleteView):
    model = Berry
    success_url = '/berries/'

def add_picking(request, berry_id):
    form = PickingForm(request.POST)
    if form.is_valid():
        new_picking = form.save(commit=False)
        new_picking.berry_id = berry_id
        new_picking.save()
    return redirect('berry-detail', berry_id=berry_id)