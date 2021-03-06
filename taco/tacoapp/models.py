from django.db import models
import datetime

class Food(models.Model) :
    date = models.DateField(auto_now=False, default=datetime.date.today)
    weekday = models.CharField(max_length=200, default='Monday')
    potato = models.IntegerField(default=0)
    bean = models.IntegerField(default=0)
    migas = models.IntegerField(default=0)
    vegan = models.IntegerField(default=0)


    def __str__(self) :
        return str(self.date)+ ' | ' + str(self.weekday) + ' | ' + str(self.potato) + ' | ' + str(self.bean) + ' | ' + str(self.migas) + ' | ' + str(self.vegan)
