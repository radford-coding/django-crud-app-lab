from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Berry
from .forms import PickingForm

# Create your views here.

# function-based views


class Home(LoginView):
    template_name = 'home.html'


def about(request):
    return render(request, 'about.html')


def berry_index(request):
    berries = request.user.berry_set.all()
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
    fields = ['name', 'variety', 'description', 'season']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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

def signup(request):
    error_msg = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('berry-index')
        else:
            error_msg = 'invalid signup - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_msg': error_msg}
    return render(request, 'signup.html', context)