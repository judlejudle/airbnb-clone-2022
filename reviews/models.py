from tkinter import CASCADE
from django.db import models
from common.models import CommonModel


class Review(CommonModel):
    """review from a user to a Room or experience"""

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey(
        "rooms.Room", null=True, blank=True, on_delete=models.SET_NULL
    )

    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    payload = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.user} / {self.rating}⭐️"
