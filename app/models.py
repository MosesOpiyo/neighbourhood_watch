from django.db import models
from django.db.models.deletion import CASCADE
from cloudinary.models import CloudinaryField

# Create your models here.


class Neighbourhood(models.Model):
    name = models.CharField(max_length = 60)
    location = models.CharField(max_length=100,null=True)
    

    def __str__(self):
        return self.name

    def create_neighbourhood(self):
        self.save()
        
    @classmethod
    def delete_neighbourhood(cls, name):
        cls.objects.filter(name=name).delete()

    @classmethod
    def find_neighbourhood(cls, search_term):
        search_results = cls.objects.filter(name__icontains = search_term)
        return search_results

    def update_neighbourhood(self, name):
        self.name = name
        self.save()

class User(models.Model):
    name = models.CharField(max_length=70)
    profile_pic = CloudinaryField(null=True,blank=True)
    email = models.EmailField()
    Neighbourhood_id = models.ForeignKey(Neighbourhood,on_delete=CASCADE)

class Neighbourhood_events(models.Model):
    event = models.TextField()
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.event

    def save_event(self):
        self.save()

    def delete_event(self):
        """This deletes the image from the database using its pk
        Args:
            id ([type]): [description]
        """
        self.delete()

class Business(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
