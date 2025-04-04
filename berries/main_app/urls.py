from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('berries/', views.berry_index, name='berry-index'),
    path('berries/<int:berry_id>/', views.berry_detail, name='berry-detail'),
    path('berries/create/', views.BerryCreate.as_view(), name='berry-create'),
    path('berries/<int:pk>/update/', views.BerryUpdate.as_view(), name='berry-update'),
    path('berries/<int:pk>/delete/', views.BerryDelete.as_view(), name='berry-delete'),
    path('berries/<int:berry_id>/add-picking/', views.add_picking, name='add-picking'),
    path('accounts/signup/', views.signup, name='signup'),
]