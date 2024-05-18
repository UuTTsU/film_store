from django.urls import path
import film
from . import views

urlpatterns = [

    path('film/',film.views.SelectFilmViews.as_view(), name='select all films'),
    path('createfilm/', film.views.CreateFilmViews.as_view(), name = 'create film'),
    path('deletefilm/<int:pk>/', film.views.DeleteFilmViews.as_view(), name='delete_film'),
    path('', views.home, name='home'),
]