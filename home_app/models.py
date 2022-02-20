from django.db import models
# the PK used is the auto increment id , django adds it by default .
class Book(models.Model):
    google_id = models.CharField(max_length=15, default = 0)
    name = models.CharField(max_length=122)
    
    author_name = models.CharField(max_length=122)
    desc = models.TextField(default=None)
    price = models.DecimalField(
                         max_digits = 8,
                         decimal_places = 2)
    qty = models.IntegerField(default=0)
    date = models.DateField()
    
    def __str__(self):
        return self.name