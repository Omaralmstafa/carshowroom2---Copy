from django.db import models

class Car(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='cars/')
    engine = models.CharField(max_length = 100)
    horsepower = models.CharField(max_length = 30)
    topspeed = models.CharField(max_length = 30)
    acceleration = models.CharField(max_length = 30)

    def __str__(self):
        return self.name
    
class CarInquiry(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    car_model = models.CharField(max_length=60)
    message = models.CharField()
    
    def __str__(self):
        return f"{self.customer_name, self.customer_email, self.car_model, self.message}"
