from django.contrib import admin
from cars import models

admin.site.register(models.Car)
admin.site.register(models.CarInquiry)