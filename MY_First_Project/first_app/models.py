from django.db import models

# Create your models here.

class Musicium(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    insrtument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name



class Album(models.Model):
    artist = models.ForeignKey(Musicium, on_delete=models.CASCADE)
    name = models.CharField(max_length= 100)
    release_date = models.DateField()

    rating =(
        (1, "worst"),
        (2, "bad"),
        (3, "not bad"),
        (4, "good"),
        (5, "Wxcellent")
    )
    num_stars = models.IntegerField(choices=rating)

    def __str__(self):
        return self.name
    
    