from django.db import models

# Create your models here.
class Product(models.Model):
    name            = models.CharField(max_length = 120)
    email           = models.EmailField(max_length = 250)
    phone_number    = models.CharField(max_length = 10)
    degree          = models.CharField(max_length = 100)
    passed_out      = models.IntegerField()
    comments        = models.TextField()

class Enrolled(models.Model):
    student_name    = models.CharField(max_length = 120, default = "")
    student_id      = models.DecimalField(max_digits = 100000000, decimal_places = 2, default = None)
    Total_Payment   = models.DecimalField(max_digits = 100000000, decimal_places = 2, default = None)
    Paid            = models.DecimalField(max_digits = 100000000, decimal_places = 2, default = None)
    Balance         = models.DecimalField(max_digits = 100000000, decimal_places = 2, default = None)
    comments        = models.TextField(default = "")