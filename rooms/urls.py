from django.urls import path
from . import views

urlpatterns = [
    path("", views.see_allRooms),
    path("<int:room_pk>", views.see_oneRoom),
]
