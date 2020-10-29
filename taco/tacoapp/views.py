from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Food
from .forms import FoodForm

def index(request) :
    if request.method == 'POST' :
        form = FoodForm(request.POST or None)

        if form.is_valid() :
            form.save()
            all_items = Food.objects.all
            return render(request, 'tacoapp/index.html', {'all_items' : all_items})

    else :
        all_items = Food.objects.all
        return render(request, 'tacoapp/index.html', {'all_items' : all_items})
