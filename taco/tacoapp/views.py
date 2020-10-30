from django.shortcuts import render, redirect
from .models import Food
from .forms import FoodForm
from django.contrib import messages
import datetime

def index(request) :

    today = str(datetime.date.today())

    if request.method == 'POST' :
        form = FoodForm(request.POST or None)

        if form.is_valid() :
            form.save()
            all_items = Food.objects.all
            context = {'all_items' : all_items,
                'today' : today}
            messages.success(request, ('Item has been logged'))
            return render(request, 'tacoapp/index.html', context)

    else :
        all_items = Food.objects.all
        context = {'all_items' : all_items,
            'today' : today}
        return render(request, 'tacoapp/index.html', context)
