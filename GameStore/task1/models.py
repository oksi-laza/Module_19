from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=5, decimal_places=2)    # размер файлов игры
    description = models.TextField()
    age_limited = models.BooleanField(default=False)    # ограничение по возрасту 18+

    # У каждого покупателя может быть несколько игр, и у каждой игры может быть несколько обладателей.
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title
