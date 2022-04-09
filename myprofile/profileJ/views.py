from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
from django.contrib import messages
import json

def indexV(request):
    person=PersonalInfo.objects.all()
    context={
        'person':person,
    }
    return render(request,'index.html',context)

def aboutV(request):
    person=PersonalInfo.objects.all()
    exper=working_Experience.objects.all()
    educ=Experince.objects.all()
    ex=Educatio.objects.all()
    context={
        'person':person,
        'exper':exper,
        'educ':educ,
        'ex':ex,
    }
    return render(request,'about.html',context)

def portfolioV(request):
    return render(request,'portfolio.html')

def contactV(request):
    persons = PersonalInfo.objects.all()
    contuct = {
        'persons':persons,
    }
    return render(request,'contact.html',contuct)

def contactsaveV(request):
    name=request.POST.get('names')
    email=request.POST.get('emails')
    subject=request.POST.get('subjects')
    message=request.POST.get('messages')
    data=datasend(Name=name,Email=email,Subject=subject,Description=message)
    data.save()
    das='success'
    # good = serializers.serialize('json', das)
    # abcs = json.loads(das)
    return JsonResponse({'result':das},status=200,safe=False)

