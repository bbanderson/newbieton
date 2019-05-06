from django.urls import path

from . import views
urlpatterns = [
    path('', views.main, name='main'),
    path('second/', views.select, name='select'),
    path('insertRecipe/', views.insertRecipe, name='insertRecipe'),
    path('menuselect/', views.menuselect, name='menuselect'),
    path('registe/', views.registe, name='registe'),

]