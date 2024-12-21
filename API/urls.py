from django.urls import path
from .import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('user-list/', views.userList, name='user-list'),
    path('user-create/', views.userRegistration, name='user-registration'),
    path('user-update/<str:pk>/', views.userUpdate, name='user-update'),
    path('user-delete/<str:pk>', views.userDelete, name='user-delete'),
    path('user-favourites/', views.userFavourites, name='user-favourites'),
    path('user-favourites-add/', views.userFavouritesAdd, name='user-favourites-add'),
    path('user-favourites-delete/', views.userFavouritesDelete, name='user-favourites-delete'),
    
]
