from django.db import models

class Food(models.Model) :
    item = models.CharField(max_length=200)

    def __str__(self) :
        return self.item
