from django.db import models
from django.urls import reverse
from django.utils import timezone
from accounts.models import User

department = (
    ('Fitness Specialist', "Fitness Specialist"),
    ('Hygiene Specialist', "Hygiene Specialist"),
    ('Pychiatric Specialist', "Psychiatric Specialist"),
    ('Mobility Specialist', 'Mobility Specialist'),
    ('Surgery Specialist', 'Surgery Specialist'),
)

gender_pet = (
    ('Male', "Male"),
    ('Female', "Female"),

)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100,)
    image = models.ImageField(null=True, blank=True)
    location = models.CharField(max_length=100,)
    start_time = models.CharField(max_length=10,)
    end_time = models.CharField(max_length=10, default =" ")
    qualification_name = models.CharField(max_length=100,)
    institute_name = models.CharField(max_length=100,)
    clinic_name = models.CharField(max_length=100,)
    department = models.CharField(choices=department, max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.full_name



class TakeAppointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100,)
    pet_name = models.CharField(max_length=100,)
    Gender_pet = models.CharField(choices=gender_pet, max_length=100,)
    message = models.TextField()
    phone_number = models.CharField(max_length=120,)
    Time_pet = models.CharField(max_length=120,)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.full_name
