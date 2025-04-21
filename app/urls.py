"""
Config urls for return diferent viwes for clients and admin
"""


from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from cars.views import cars_view, new_car_view

urlpatterns = [
    path('', cars_view, name='home'),
    path('admin/', admin.site.urls),
    path('cars/', cars_view, name='cars'),
    path("new_car/", new_car_view, name="new_car")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
