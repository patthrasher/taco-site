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
        weekdays = ('Sunday', 'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
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


        # plst = []
        # blst = []
        # for each in sun  :
        #     plst.append(each.potato)
        #     blst.append(each.bean)


        # sun_pot_tot = sum(plst)
        # sun_bean_tot = sum(blst)
        #
        # sun_pot_av = sun_pot_tot // len(plst)
        # sun_bean_av = sun_bean_tot // len(blst)

        sun = Food.objects.filter(weekday='Sunday')
        mon = Food.objects.filter(weekday='Monday')
        tue = Food.objects.filter(weekday='Tuesday')
        wed = Food.objects.filter(weekday='Wednesday')
        thu = Food.objects.filter(weekday='Thursday')
        fri = Food.objects.filter(weekday='Friday')
        sat = Food.objects.filter(weekday='Saturday')


        sun_dic = {'pot' : [], 'bean' : []}

        # for each in sun :
        #     sun_dic['pot'].append(each.potato)
        #     sun_dic['bean'].append(each.bean)

        sun_dic['pot'] = [i.potato for i in sun]
        sun_dic['bean'] = [i.bean for i in sun]


        l = len(sun_dic['pot'])
        sun_dic['pot'] = sum(sun_dic['pot']) // l
        sun_dic['bean'] = sum(sun_dic['bean']) // l



        mon_dic = {'pot' : [], 'bean' : []}

        # for each in mon :
        #     mon_dic['pot'].append(each.potato)
        #     mon_dic['bean'].append(each.bean)

        mon_dic['pot'] = [i.potato for i in mon]
        mon_dic['bean'] = [i.potato for i in mon]

        l = len(mon_dic['pot'])
        mon_dic['pot'] = sum(mon_dic['pot']) // l
        mon_dic['bean'] = sum(mon_dic['bean']) // l


        # try all in one dic
        # big_dic = {
        #     'sun' : {'pot' : [], 'bean' : []},
        #     'mon' : {'pot' : [], 'bean' : []},
        #     'tue' : {'pot' : [], 'bean' : []},
        # }
        #
        # def som(obj, taco, day) :
        #     for each in obj :
        #         big_dic[day][taco].append(each.potato)
        #     return big_dic
        #
        # ok = som(tue, 'pot', 'tue')


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
            # 'fil' : fil,
            # 'plst' : plst,
            # 'blst' : blst,
            # 'sun_bean_tot' : sun_bean_tot,
            # 'sun_pot_tot' : sun_pot_tot,
            # 'sun_bean_av' : sun_bean_av,
            # 'sun_pot_av' : sun_pot_av,
            # 'test_lst' : test_lst,
            'sun_dic' : sun_dic,
            'mon_dic' : mon_dic,
            'weekdays' : weekdays,
            # 'ok' : ok,
            'sun' : sun,
        }

        return render(request, 'tacoapp/manager.html', context)
