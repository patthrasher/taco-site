from django import forms
from .models import Food

class food_form(forms.ModelForm) :
    class Meta :
        model = Food
        fields = ['date', 'potato', 'bean', 'weekday', 'migas', 'vegan']

# class sheets_test(forms.ModelForm) :
#     class Meta :
#         model =
