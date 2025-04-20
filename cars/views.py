from django.shortcuts import render
from cars.models import Car, Brand

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
