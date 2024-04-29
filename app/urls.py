from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('villa_list/', views.VillaListView.as_view(), name='villa_list'),
    path('villa_detail/<int:pk>/', views.villa_detail_view, name='villa_detail'),
    path('villa_update/<int:pk>/', views.villa_update_view, name='villa_update'),
    path('villa_delete/<int:pk>/', views.villa_delete_view, name='villa_delete'),
]
