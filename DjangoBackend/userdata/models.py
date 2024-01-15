from django.db import models

from accounts.models import User
from recipes.models import Recipe
from django.utils import timezone


# Create your models here.
class Rating(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='rated', default=None)
    recipe = models.ForeignKey(to=Recipe, on_delete=models.CASCADE, related_name='rated', default=None)
    score = models.IntegerField()


class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='commented', default=None)
    recipe = models.ForeignKey(to=Recipe, on_delete=models.CASCADE, related_name='commented', default=None)
    message = models.TextField(max_length=500)
    file = models.FileField(upload_to='comment/', null=True, blank=True)
    createdDate = models.DateTimeField(default=timezone.now)


class LikedRecipe(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='liked', default=None)
    recipe = models.ForeignKey(to=Recipe, on_delete=models.CASCADE, related_name='liked', default=None)

class FavoritedRecipe(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='favorited', default=None)
    recipe = models.ForeignKey(to=Recipe, on_delete=models.CASCADE, related_name='favorited', default=None)


class BrowsedRecipe(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='browsed', default=None)
    recipe = models.ForeignKey(to=Recipe, on_delete=models.CASCADE, related_name='browsed', default=None)


class ShoppingList(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='lst', default=None)
    recipe = models.ForeignKey(to=Recipe, on_delete=models.CASCADE, related_name='lst', default=None)
    number = models.IntegerField(default=1)