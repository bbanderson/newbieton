from django.shortcuts import render
from django.views.generic. base import TemplateView

# Create your views here.
# class MainpageView(TemplateView):
#     template_name = 'theme/main.html'

def main(request):
    return render(request, 'theme/main.html')

def select(request):
    return render(request, 'theme/second.html')

# def insertRecipe(request):
#     return render(request, 'theme/insertRecipe.html')

# def menuselect(request):
#     return render(request, 'theme/menuselect.html')

# def registe(request):
#     return render(request, 'theme/registe.html')
