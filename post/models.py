from django.db import models


class LostPet(models.Model):
    pub_date = models.DateTimeField('date published')
    pub_name = models.CharField(max_length=200)
    pub_phone = models.CharField(max_length=200)
    pub_email = models.CharField(max_length=200)
    animal_type = models.CharField(max_length=200)
    animal_status = models.CharField(max_length=200)
    animal_location = models.CharField(max_length=200)
    animal_freetext = models.CharField(max_length=200)
    animal_image = models.ImageField(upload_to ='media/uploads/')
    def __str__(self):
        return self.pub_name
        
class Comment(models.Model):
    pet = models.ForeignKey(LostPet, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    freetext = models.CharField(max_length=10000)


