from django.shortcuts import render, redirect
from cars.models import Car, Brand
from cars.forms import CarForm
from django.views import View

class CarsView(View):
    def get(self, request):
        cars = Car.objects.all().order_by("model")
        search = request.GET.get("search")

        if search:
            cars = cars.filter(model__icontains=search)

        return render(
            request,
            "cars.html",
            {"cars": cars}
        )

class NewCarView(View):
    def get(self, request):
        form = CarForm()
        return render(request, "new_car.html", {"new_car_form": form})

    def post(self, request):
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("cars")  # ou 'cars_list', se for esse o nome da sua URL
        return render(request, "new_car.html", {"new_car_form": form}) 