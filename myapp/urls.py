from django.urls import path
from . import views

urlpatterns = [
    path('my-menu-page/', views.my_menu_page, name='my_menu_page'),
]
