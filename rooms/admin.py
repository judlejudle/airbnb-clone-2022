from django.contrib import admin
from .models import Room, Amenity


@admin.register(Room)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "kind",
        "owner",
    )
    list_filter = (
        "country",
        "city",
        "pet_friendly",
        "kind",
        "owner",
        "amenities",
    )


@admin.register(Amenity)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
