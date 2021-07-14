## Just the methods for brands
from django.shortcuts import render, redirect, HttpResponse
from .models import Brand, Car
from .forms import BrandForm, CarForm

def get_brand(brand_id):
    return Brand.objects.get(id=brand_id)

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'brands/brands_list.html', {'brands': brands})

def brand_detail(request, brand_id):
    brand = get_brand(brand_id)
    return render(request, 'brands/brand_detail.html', {'brand': brand})

def new_brand(request):
    if request.method == "POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()
            return redirect('brand_detail', brand_id=brand.id)
    else:
        form = BrandForm()
    return render(request, 'brands/brand_form.html', {'form': form, 'type_of_request': 'New'})

def edit_brand(request, brand_id):
    brand = get_brand(brand_id)
    if request.method == "POST":
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()
            return redirect('brand_detail', brand_id=brand.id)
    else:
        form = BrandForm(instance=brand)
    return render(request, 'brands/brand_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_brand(request, brand_id):
    if request.method == "POST":
        brand = get_brand(brand_id)
        brand.delete()
    return redirect('brand_list')

def get_car(car_id):
    return Car.objects.get(id=car_id)

def car_list(request, brand_id):
    brand = get_brand(brand_id)
    cars = brand.cars.all()
    return render(request, 'cars/cars_list.html', {'brand': brand, 'cars': cars})

def car_detail(request, brand_id, car_id):
    brand = get_brand(brand_id)
    car = get_car(car_id)
    return render(request, 'cars/car_detail.html', {'brand': brand, 'car': car})

def new_car(request, brand_id):
    brand = get_brand(brand_id)
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.brand = brand
            car.save()
            return redirect('car_detail', brand_id=car.brand.id, car_id=car.id)
    else:
        form = CarForm()
    return render(request, 'cars/car_form.html', {'form': form, 'type_of_request': 'New'})

def edit_car(request, brand_id, car_id):
    brand = get_brand(brand_id)
    car = get_car(car_id)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            return redirect('car_detail', car_id=car.id, brand_id=brand_id)
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/car_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_car(request, brand_id, car_id):
    if request.method == "POST":
        car = get_car(car_id)
        car.delete()
    return redirect('car_list', brand_id=brand_id)