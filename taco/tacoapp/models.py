from django.db import models
import datetime

class Food(models.Model) :
    date = models.DateField(auto_now=False, default=datetime.date.today)
    item = models.CharField(max_length=200)
    number = models.IntegerField(default=99)

    def __str__(self) :
        return str(self.date) + ' | ' + self.item + ' | ' + str(self.number)
