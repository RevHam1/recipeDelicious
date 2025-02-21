from django.urls import path
from . import views

urlpatterns = [
    ## Register & Login
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('recipe_cards/', views.recipe),

    ## APP specific Routes
    path('save', views.save),
    path('recipes_saved', views.recipes_saved),
    path('recipes_index', views.recipes_index),
    path('recipe_card/<int:card_id>', views.show_card),
    path('delete/<int:card_id>', views.delete),

    path('recipe_card/like/<int:card_id>', views.like_card),
    path('recipe_card/unlike/<int:card_id>', views.unlike_card),
]