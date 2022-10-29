from django.contrib import admin
from django.urls import path, include
from rooms import views
from django.conf.urls.static import static
from django.conf import settings

# 어드민 페이지 이상해서 3.1에 업데이트 된 내용 disable 시킴
admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/rooms/", include("rooms.urls")),
    path("api/v1/categories/", include("categories.urls")),
    path("api/v1/experiences/", include("experiences.urls")),
    path("api/v1/medias/", include("medias.urls")),
    path("api/v1/wishlists/", include("wishlists.urls")),
    path("api/v1/users/", include("users.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
