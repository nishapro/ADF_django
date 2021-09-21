from django.db import models

# Create your models here.

class requestTable(models.Model):
    first_name = models.CharField(max_length=50)
    mid_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    current_city = models.CharField(max_length=50)
    pincode = models.IntegerField()
    qualification = models.CharField(max_length=50)
    salary = models.IntegerField()
    pan = models.CharField(max_length=50)
    request_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'request_form'

class responseTable(models.Model):
    request_id = models.IntegerField()
    response = models.CharField(max_length=50)
    reason = models.CharField(max_length=300)

    class Meta:
        db_table = 'response_form'




