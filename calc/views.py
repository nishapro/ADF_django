from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
import json
from .models import requestTable, responseTable
from calc import models
from . import validate
from .forms import RequestForm
from . import views

# Create your views here.

def home(request):
    form = RequestForm()
    if request.method == 'POST':
        form=RequestForm(request.POST)
        if form.is_valid():
           form.save()
    return render(request, 'home.html', {'form': form})


def storeDetails(request):
    req = requestTable()
    res = responseTable()
    user = validate.userData( first_name = request.POST['first_name'],mid_name = request.POST['mid_name'],
                              last_name = request.POST['last_name'], dob = request.POST['dob'] ,
                              gender = request.POST['gender'] , nationality = request.POST['nationality'],
                              current_city = request.POST['current_city'] , state = request.POST['state'],
                              pincode = request.POST['pincode'] , qualification = request.POST['qualification'] ,
                              salary = request.POST['salary'] , pan = request.POST['pan'] )
    user.validate_details()

    req.first_name = user.first_name
    req.mid_name = user.mid_name
    req.last_name = user.last_name
    req.dob = user.dob
    req.gender = user.gender
    req.nationality = user.nationality
    req.current_city = user.current_city
    req.state = user.state
    req.pincode = user.pincode
    req.qualification = user.qualification
    req.salary = user.salary
    req.pan = user.pan


    req.save()
    res.request_id = requestTable.objects.latest('id').id
    res.response = user.result
    res.reason = user.reason
    res.save()

    dictionary={}
    if res.response=="success":
        dictionary["request_id"]=res.request_id
        dictionary["response"]=res.response
    elif res.response == "failure":
        dictionary["request_id"] = res.request_id
        dictionary["response"] = res.response
        dictionary["reason"] = res.reason

    dumping=json.dumps(dictionary)

    return render(request,'result.html',{'result':dumping})
