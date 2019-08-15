from django.db import models

class Destination(models.Model):
    # _id         : int
    # name        : str
    # img         : str
    # description : str
    # price       : float
    # offer       : bool
    name        = models.CharField(max_length = 100)
    img         = models.ImageField(upload_to = 'pics')
    description = models.TextField()
    price       = models.FloatField()
    offer       = models.BooleanField(default = False)


    # python manage.py makemigrations
    # python manage.py migrate
