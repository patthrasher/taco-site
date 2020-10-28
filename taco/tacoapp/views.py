from django.shortcuts import render
from django.http import HttpResponse
from .forms import FoodForm

def index(request) :
    if request.method == 'POST' :
        form = FoodForm(request.POST or None)

        if form.is_valid() :
            form.save()
            all_items = Food.objects.all
            return render(request, 'tacoapp/index.html', {'all_items' : 'something to display'})

    else :
        return render(request, 'tacoapp/index.html', {'all_items' : 'nothing to display'})
