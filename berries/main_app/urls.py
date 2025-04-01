from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('berries/', views.berry_index, name='berry-index'),
    path('berries/<int:berry_id>/', views.berry_detail, name='berry-detail'),
]