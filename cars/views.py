from django.shortcuts import render, redirect
from cars.models import Car, Brand
from cars.forms import CarForm
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'


class HomeView(TemplateView):
    template_name = "home.html"

    
class CarsListView(ListView):
    model = Car
    template_name = "cars.html"
    context_object_name = "cars"

    def get_queryset(self):
        cars = super().get_queryset().order_by("model")
        search = self.request.GET.get("search")
        if search:
            cars = cars.filter(model__icontains=search)
        return cars

        

class NewCarView(CreateView):
    model = Car
    form_class = CarForm
    template_name = "new_car.html"
    success_url = reverse_lazy("cars")
    context_object_name = "new_car_form"