from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=450)
    email = models.EmailField(unique=True)
    Password = models.CharField(max_length=32, null=False)

    def __str__(self):
        return self.email


class Ingredient(models.Model):
    name = models.CharField(max_length=450)

#     def __str__(self):
#         return self.name


# # class Recipe(models.Model):
# #     title = models.CharField(max_length=450)
# #     food_name = models.CharField(max_length=200)
# #     ingredients = models.ManyToManyField(Ingredient)
# #     food_img = models.ImageField(blank=True)
# #     recipe_description = models.CharField(
# #         max_length=500, null=True, blank=True)
# #     cooking_time = models.IntegerField(default=5)
# #     u_id = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title



