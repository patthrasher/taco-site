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

        return render(request, 'tacoapp/index.html', context)

@login_required
def manager(request) :

    if not request.user.username == 'sarah' :
        messages.success(request, ('You sir do not have access to that page!'))
        return redirect('tacoapp:index')

    else :
        all_items = Food.objects.all
        context = {'all_items' : all_items}
        return render(request, 'tacoapp/manager.html', context)
