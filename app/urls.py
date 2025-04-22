"""
Config urls for return diferent viwes for clients and admin
"""
from accounts.views import CustomLoginView

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from cars.views import CarsView, NewCarView
from accounts.views import register_view
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('', CarsView.as_view(), name='home'),  # página inicial usa a CBV
    path('admin/', admin.site.urls),
    path('cars/', CarsView.as_view(), name='cars'),  # rota de listagem de carros
    path('new_car/', NewCarView.as_view(), name='new_car'),  # cadastro de carro
    path('register/', register_view, name='register'),  # cadastro de usuário
    path('login/', CustomLoginView.as_view(), name='login'),  # login customizado
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # logout
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)