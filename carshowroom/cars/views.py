import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
from django.shortcuts import render, get_object_or_404
from .models import Car
from django.views.decorators.csrf import csrf_exempt
from .models import CarInquiry
# Create your views here.
def get_cars(request):
    if request.method == "GET":
        data = list(models.Car.objects.values())
        return JsonResponse(data, safe=False)
      

    
@csrf_exempt
def add_car(request):
    if request.method == "POST":
        data = json.loads(request.body)
        car = models.Car(
        name = data.get("name"),
        acceleration = data.get("acceleration"),
        description = data.get("description"),
        engine = data.get("engine"),
        horsepower = data.get("horsepower"),
        image = data.get("image"),        
        topSpeed = data.get("topSpeed")
        )
        car.save()
        return JsonResponse({ "message": "OK", "id": car.id }) 
      


def home(request):
    cars = Car.objects.all()
    return render(request, 'pages/index.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'pages/car-template.html', {'car': car})


@csrf_exempt
def add_inquiry(request):
    if request.method == "POST":
        data = json.loads(request.body)
        inquiry = CarInquiry.objects.create(
            customer_name=data.get("name"),
            customer_email=data.get("email"),
            car_model=data.get("carModel"),
            message=data.get("message")
        )
        return JsonResponse({"message": "تم إرسال الاستفسار بنجاح!"})
    return JsonResponse({"error": "Invalid request"}, status=400)
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect

@staff_member_required
def car_edit(request, car_id):
    car = get_object_or_404(Car, id=car_id)
   
    if request.method == "POST":
        car.name = request.POST.get("name")
        car.description = request.POST.get("description")
        car.save()
        return redirect('car_detail', car_id=car.id)
    return render(request, "pages/car_edit.html", {"car": car})

@staff_member_required
def car_delete(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == "POST":
        car.delete()
        return redirect('home')
    return render(request, "pages/car_confirm_delete.html", {"car": car})
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .models import Car

@staff_member_required
def car_add(request):
    if request.method == "POST":
        Car.objects.create(
            name=request.POST.get("name"),
            description=request.POST.get("description"),
            image=request.FILES.get("image"),
            engine=request.POST.get("engine"),
            horsepower=request.POST.get("horsepower"),
            topSpeed=request.POST.get("topSpeed"),
            acceleration=request.POST.get("acceleration"),
        )
        return redirect('home')
    return render(request, "pages/car_add.html")
from .models import CarInquiry
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def inquiries_list(request):
    inquiries = CarInquiry.objects.all().order_by('-id')
    return render(request, "pages/inquiries_list.html", {"inquiries": inquiries})
from django.shortcuts import get_object_or_404, redirect
from .models import CarInquiry
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def delete_inquiry(request, inquiry_id):
    inquiry = get_object_or_404(CarInquiry, id=inquiry_id)
    if request.method == "POST":
        inquiry.delete()
    return redirect('inquiries_list')
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'pages/login.html'