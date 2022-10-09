from django.shortcuts import render
from django.http import HttpResponse
from rooms.models import Room

# Create your views here.


def see_allRooms(request):
    rooms = Room.objects.all()
    return render(
        request,
        "all_rooms.html",
        {"rooms": rooms, "title": "hello this title comes from django"},
    )


def see_oneRoom(request, room_pk):
    try:
        room = Room.objects.get(pk=room_pk)
        return render(
            request,
            "room_detail.html",
            {
                "room": room,
            },
        )
    except Room.DoesNotExist:
        return render(
            request,
            "room_detail.html",
            {
                "not_found": True,
            },
        )
