"""
Config urls for return diferent viwes for clients and admin
"""
from accounts.views import CustomLoginView

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from cars.views import NewCarView, CarsListView
from accounts.views import register_view
from django.contrib.auth.views import LoginView, LogoutView
from cars.views import HomeView
from cars.views import CarDetailView



urlpatterns = [
    path('admin/', admin.site.urls),
    path("car/<int:pk>/", CarDetailView.as_view(), name="car_detail"),
    path('', HomeView.as_view(), name='home'),
    path('cars/', CarsListView.as_view(), name='cars'),  # rota de listagem de carros
    path("new_car/", NewCarView.as_view(), name="new_car"), # cadastro de carro
    path('register/', register_view, name='register'),  # cadastro de usuário
    path('login/', CustomLoginView.as_view(), name='login'),  # login customizado
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # logout
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)