from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET,require_POST
import json
from .models import *
from datetime import timedelta,datetime
from login.models import *
eror=0
time='23:59:59'
finish='00:00:00'
finish=datetime.strptime(finish,'%H:%M:%S')
time=datetime.strptime(time,'%H:%M:%S')
@csrf_exempt
@require_POST
def login_manage(request):
    global eror
    data=json.loads(request.body.decode('UTF-8'))
   # manage.objects.create(
    #    name=data['name'],
     #   password=data['password']
    #)
    print(eror)
    for i in manage.objects.all():
        if data['name']==i.name and data['password']==i.password:
            return JsonResponse({
                'result':True
            })
        
        elif eror!=3 or eror>=3 :
            eror+=1
            if eror==3 or eror>=3:
                return JsonResponse({
                    'result':'run'
                })
            else:
                return JsonResponse({
                    'result':False
                })
@require_GET
def timing(request):
    global time,eror
    
    time=time-timedelta(seconds=1)
    print(time)
    if finish==time:
        eror=0
        return JsonResponse({
            'result':'open'
        })
    else:
        return JsonResponse({
            'result':time.strftime('%H:%M:%S')
        })

def show_user(request):
    data=[]
    number=0
    for i in users.objects.all():
        number+=1
        data_user={
            'name':i.name,
            'number':i.number,
            'age':i.age,
            'password':i.password,
            'gender':i.gender,
            'accept':i.accept,
            'regestration':i.regestration

        }
        data.append(data_user)
    return JsonResponse({
        'population':number,
        'result':data
    })
@csrf_exempt
@require_POST
def search_user(request):
    data=json.loads(request.body)
    print(data)
    search=users.objects.filter(number=data['data'])
    if search:
        data_user=[]
        for i in users.objects.all().filter(number=data['data']):
            data_user.append({
                'name':i.name,
                'number':i.number,
                'age':i.age,
                'password':i.password,
                'gender':i.gender,
                'accept':i.accept,
                'regestration':i.regestration

             })
        return JsonResponse({
            'ans':True,
            'result':data_user
        })
    else:
        return JsonResponse({
            'ans':False,
        })

 #let data={'phone':one,'text':two}


    






# Create your views here.
