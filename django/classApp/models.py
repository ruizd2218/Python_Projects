from django.db import models

#creating our class model that we can use to make more objects inside of our website
class DjangoClasses(models.Model):
    title = models.CharField(max_length=50)
    courseNumber = models.IntegerField(default=0)
    instructor = models.CharField(max_length=70)
    duration = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)


