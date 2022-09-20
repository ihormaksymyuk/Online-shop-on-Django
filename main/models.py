from django.db import models

# Create your models here.
class Catalog(models.Model):
    title = models.CharField('Назва товару', max_length=50)
    description = models.TextField('Опис товару')
    price = models.FloatField('Ціна')

    def __str__(self):
        return self.title