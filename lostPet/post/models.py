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
    animal_image = models.ImageField(upload_to ='uploads/')
    def __str__(self):
        return self.pub_name
    


