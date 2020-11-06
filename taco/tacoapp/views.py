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

        def som(dayy, food, obj) :
            if day == dayy :
                counts[food] = counts[food] + obj.potato
            return counts

        all_items = Food.objects.all()

        for each in all_items :
            total = total + each.number

        weekdays = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
        foods = ['potato', 'bean']
        counts = {'potato' : [0, 0], 'bean' : [0, 0]}

        wedcount = 0
        thucount = 0

        lst = []
        for each in all_items :
            day = weekdays[each.date.weekday()]
            # dayday = day.weekday()
            # daystring = weekDays[day]
            lst.append(day)

            num = each.potato

            if day == 'Wednesday' :
                wedcount = wedcount + num


        dc = {}
        for each in weekdays :
            # count = lst.count(each)
            dc.update({each : counts})

            # {'potato' : [wedcount, lst.count(each)]

        # dctot = {}
        # for each in weekdays :
        #     count = lst.count()

        # av = dc['Wednesday']['potato'][0] / dc['Wednesday']['potato'][1]

        context = {
            'all_items' : all_items,
            'total' : total,
            'list' : lst,
            'dc' : dc,
            'wedcount' : wedcount,
            # 'av' : av,
        }

        return render(request, 'tacoapp/manager.html', context)
