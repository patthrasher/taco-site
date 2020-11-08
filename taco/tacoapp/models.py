from django.db import models
import datetime

class Food(models.Model) :
    date = models.DateField(auto_now=False, default=datetime.date.today)
    potato = models.IntegerField(default=10)
    bean = models.IntegerField(default=5)

    def __str__(self) :
        return str(self.date)+ ' | ' + str(self.potato) + ' | ' + str(self.bean)
