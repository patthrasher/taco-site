from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Food
from .forms import FoodForm
from django.contrib import messages
import datetime

from django.contrib.auth.decorators import login_required

import pandas as pd

@login_required
def index(request) :

    today = str(datetime.date.today())

    if request.method == 'POST' :
        form = FoodForm(request.POST or None)

        if form.is_valid() :
            form.save()
            all_items = Food.objects.all
            messages.success(request, ('Item has been logged'))
            return redirect('tacoapp:index')
    else :
        context = {
            'today' : today,
        }
        return render(request, 'tacoapp/index.html', context)

@login_required
def manager(request) :

    total = 0

    if not request.user.username == 'sarah' :
        messages.success(request, ('You sir do not have access to that page!'))
        return redirect('tacoapp:index')

    else :

        all_items = Food.objects.all()
        weekdays = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
        foodcount = {'potato' : 0, 'bean' : 0}


        dic = {all_items}
        daylist = []
        for each in all_items :
            day = weekdays[each.date.weekday()]
            daylist.append(day)

        daycount = {}
        for each in weekdays :
            count = daylist.count(each)
            daycount.update({each : count})


        potlist = []
        beanlist = []
        for each in all_items :
            potlist.append(each.potato)
            beanlist.append(each.bean)

        pottot = sum(potlist)
        beantot = sum(beanlist)

        total = pottot + beantot

        x = Food.objects.raw('Select * FROM tacoapp_food')


        context = {
            'all_items' : all_items,
            'daylist' : daylist,
            'daycount' : daycount,
            'potlist' : potlist,
            'pottot' : pottot,
            'beanlist' : beanlist,
            'beantot' : beantot,
            'total' : total,
            'dic' : dic,
            'x' : x,
        }

        return render(request, 'tacoapp/manager.html', context)
