from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .insertForm import RecipeForm
from .models import Recipe, User, Ingredient

def index(request):
    return render(request, "index.html")

def registe(request):
    recipes = Recipe.objects
    return render(request, 'registe.html', {'recipes': recipes})

# def insertRecipe(request):
#     return render(request, 'insertRecipe.html')

# def recipeform(request, recipe=None):
#     if request.method == "POST":
#         form = RecipeForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             print(1)
#             recipe = form.save(commit=False)
#             user = User.objects.filter(email="minjony1014@gmail.com").last()
#             if user is None:
#                 return HttpResponse('error00')
#             recipe.u_id = user
#             recipe.save()
#             return redirect('registe')
#         else:
#             return HttpResponse('something wrong')
#     else:
#         # instance=blog는 없어도 되는데 뒤에 edit에서 사용하기 위함
#         form = RecipeForm()
#         return render(request, 'insertRecipe.html', {'form': form})
                                                     
# # def selectRecipe(request):
# #     ingredient = Ingredient.objects
# #     return render(request, 'selectRecipe.html', {'ingredients': ingredient})

# # def selectResult(request):
# #     ingredents = request.GET['ingredients']
# #     recipes = Recipe.objects.filter(ingredients=ingredents)
# #     return render(request, 'selectResult.html',  {'recipes': recipes})