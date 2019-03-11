

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('newUser/', views.newUser, name="newUser"),
    path('addRecipe/', views.addRecipe, name="addRecipe"),
    path('recipeInfo/', views.recipeInfo, name="recipeInfo"),
    path('editRecipe/<int:recipeID>/', views.editRecipe, name="editRecipe"),
    path('deleteRecipe/<int:recipeID>/', views.deleteRecipe, name="deleteRecipe"),

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]



