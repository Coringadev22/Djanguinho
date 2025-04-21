from django.shortcuts import render, redirect
from cars.models import Car, Brand
from cars.forms import CarForm

def cars_view(request):
    selected_brand = request.GET.get("brand", "")
    brands = Brand.objects.all()

    if selected_brand:
        cars = Car.objects.filter(brand__name__iexact=selected_brand)
    else:
        cars = Car.objects.all()

    return render(request, "cars.html", {
        "cars": cars,
        "brands": brands,
        "selected_brand": selected_brand
    })


def new_car_view(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Salvamento centralizado no formulário
            return redirect('cars')
    else:
        form = CarForm()

    return render(request, "new_car.html", {"new_car_form": form})
