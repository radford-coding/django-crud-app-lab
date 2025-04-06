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
    path('farms/create', views.FarmCreate.as_view(), name='farm-create'),
    path('farms/<int:pk>/', views.FarmDetail.as_view(), name='farm-detail'),
    path('farms/', views.FarmList.as_view(), name='farm-index'),
    path('farms/<int:pk>/update/', views.FarmUpdate.as_view(), name='farm-update'),
    path('farms/<int:pk>/delete/', views.FarmDelete.as_view(), name='farm-delete'),
    path('berries/<int:berry_id>/associate-farm/<int:farm_id>/', views.associate_farm, name='associate-farm'),
    path('berries/<int:berry_id>/remove-farm/<int:farm_id>/', views.remove_farm, name='remove-farm'),
    path('accounts/signup/', views.signup, name='signup'),
]