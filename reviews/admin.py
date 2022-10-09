from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "filter by words"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            reviews


class BadReviewFilter(admin.SimpleListFilter):
    title = "filter bad reviews"
    parameter_name = "Bad"

    def lookups(self, request, model_admin):
        return [
            ("worst", "Worst"),
            ("bad", "bad"),
            ("great", "great"),
        ]

    def queryset(self, request, parameter):
        print(dir(self.value()))
        if self.value() == "worst":
            return parameter.filter(rating__lte=1)
        if self.value() == "bad":
            return parameter.filter(rating__lte=3)
        if self.value() == "great":
            return parameter.filter(rating__lte=5)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
    )

    list_filter = (
        WordFilter,
        BadReviewFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
