from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Food
from .forms import FoodForm
from django.contrib import messages
import datetime

from django.contrib.auth.decorators import login_required


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

        all_tacos_lists = [[i.potato for i in all_items], [i.bean for i in all_items],
            [i.migas for i in all_items], [i.vegan for i in all_items]]

        total = sum(map(sum, all_tacos_lists))


        sun = Food.objects.filter(weekday='Sunday')
        mon = Food.objects.filter(weekday='Monday')
        tue = Food.objects.filter(weekday='Tuesday')
        wed = Food.objects.filter(weekday='Wednesday')
        thu = Food.objects.filter(weekday='Thursday')
        fri = Food.objects.filter(weekday='Friday')
        sat = Food.objects.filter(weekday='Saturday')


        # Sunday
        sun_dic = {'pot' : [], 'bean' : [], 'migas' : [], 'vegan' : []}

        sun_dic['pot'] = [i.potato for i in sun]
        sun_dic['bean'] = [i.bean for i in sun]
        sun_dic['migas'] = [i.migas for i in sun]
        sun_dic['vegan'] = [i.vegan for i in sun]

        l = len(sun_dic['pot'])
        if l == 0 :
            mes = 'Yo can\'t divide by zero bud'
        else :
            sun_dic['pot'] = sum(sun_dic['pot']) // l
            sun_dic['bean'] = sum(sun_dic['bean']) // l
            sun_dic['migas'] = sum(sun_dic['migas']) // l
            sun_dic['vegan'] = sum(sun_dic['vegan']) // l
            mes = ''


        # Monday
        mon_dic = {'pot' : [], 'bean' : [], 'migas' : [], 'vegan' : []}

        mon_dic['pot'] = [i.potato for i in mon]
        mon_dic['bean'] = [i.potato for i in mon]
        mon_dic['migas'] = [i.migas for i in mon]
        mon_dic['vegan'] = [i.vegan for i in mon]

        l = len(mon_dic['pot'])
        if l == 0 :
            mes = 'Yo cant divide by zero bud'
        else :
            mon_dic['pot'] = sum(mon_dic['pot']) // l
            mon_dic['bean'] = sum(mon_dic['bean']) // l
            mon_dic['migas'] = sum(mon_dic['migas']) // l
            mon_dic['vegan'] = sum(mon_dic['vegan']) // l
            mes = ''

        # Tuesday
        tue_dic = {'pot' : [], 'bean' : [], 'migas' : [], 'vegan' : []}

        tue_dic['pot'] = [i.potato for i in tue]
        tue_dic['bean'] = [i.bean for i in tue]
        tue_dic['migas'] = [i.migas for i in tue]
        tue_dic['vegan'] = [i.vegan for i in tue]

        l = len(tue_dic['pot'])
        if l == 0 :
            mes = 'Yo can\'t divide by zero bud'
        else :
            tue_dic['pot'] = sum(tue_dic['pot']) // l
            tue_dic['bean'] = sum(tue_dic['bean']) // l
            tue_dic['migas'] = sum(tue_dic['migas']) // l
            tue_dic['vegan'] = sum(tue_dic['vegan']) // l
            mes = ''


        # Wednesday
        wed_dic = {'pot' : [], 'bean' : [], 'migas' : [], 'vegan' : []}

        wed_dic['pot'] = [i.potato for i in wed]
        wed_dic['bean'] = [i.bean for i in wed]
        wed_dic['migas'] = [i.migas for i in wed]
        wed_dic['vegan'] = [i.vegan for i in wed]

        l = len(wed_dic['pot'])
        if l == 0 :
            mes = 'Yo can\'t divide by zero bud'
        else :
            wed_dic['pot'] = sum(wed_dic['pot']) // l
            wed_dic['bean'] = sum(wed_dic['bean']) // l
            wed_dic['migas'] = sum(wed_dic['migas']) // l
            wed_dic['vegan'] = sum(wed_dic['vegan']) // l
            mes = ''


        # Thursday
        thu_dic = {'pot' : [], 'bean' : [], 'migas' : [], 'vegan' : []}

        thu_dic['pot'] = [i.potato for i in thu]
        thu_dic['bean'] = [i.bean for i in thu]
        thu_dic['migas'] = [i.migas for i in thu]
        thu_dic['vegan'] = [i.vegan for i in thu]

        l = len(thu_dic['pot'])
        if l == 0 :
            mes = 'Yo can\'t divide by zero bud'
        else :
            thu_dic['pot'] = sum(thu_dic['pot']) // l
            thu_dic['bean'] = sum(thu_dic['bean']) // l
            thu_dic['migas'] = sum(thu_dic['migas']) // l
            thu_dic['vegan'] = sum(thu_dic['vegan']) // l
            mes = ''


        # Friday
        fri_dic = {'pot' : [], 'bean' : [], 'migas' : [], 'vegan' : []}

        fri_dic['pot'] = [i.potato for i in fri]
        fri_dic['bean'] = [i.bean for i in fri]
        fri_dic['migas'] = [i.migas for i in fri]
        fri_dic['vegan'] = [i.vegan for i in fri]

        l = len(fri_dic['pot'])
        if l == 0 :
            mes = 'Yo can\'t divide by zero bud'
        else :
            fri_dic['pot'] = sum(fri_dic['pot']) // l
            fri_dic['bean'] = sum(fri_dic['bean']) // l
            fri_dic['migas'] = sum(fri_dic['migas']) // l
            fri_dic['vegan'] = sum(fri_dic['vegan']) // l
            mes = ''


        # Saturday
        sat_dic = {'pot' : [], 'bean' : [], 'migas' : [], 'vegan' : []}

        sat_dic['pot'] = [i.potato for i in sat]
        sat_dic['bean'] = [i.bean for i in sat]
        sat_dic['migas'] = [i.migas for i in sat]
        sat_dic['vegan'] = [i.vegan for i in sat]

        l = len(sat_dic['pot'])
        if l == 0 :
            mes = 'Yo can\'t divide by zero bud'
        else :
            sat_dic['pot'] = sum(sat_dic['pot']) // l
            sat_dic['bean'] = sum(sat_dic['bean']) // l
            sat_dic['migas'] = sum(sat_dic['migas']) // l
            sat_dic['vegan'] = sum(sat_dic['vegan']) // l
            mes = ''

        context = {
            'all_items' : all_items,
            # 'daylist' : daylist,
            # 'daycount' : daycount,
            # 'potlist' : potlist,
            # 'pottot' : pottot,
            # 'beanlist' : beanlist,
            # 'beantot' : beantot,
            'total' : total,
            # 'dic' : dic,
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
            'tue_dic' : tue_dic,
            'wed_dic' : wed_dic,
            'thu_dic' : thu_dic,
            'fri_dic' : fri_dic,
            'sat_dic' : sat_dic,
            # 'weekdays' : weekdays,
            # 'ok' : ok,
            # 'sun' : sun,
            'mes' : mes,
        }

        return render(request, 'tacoapp/manager.html', context)
