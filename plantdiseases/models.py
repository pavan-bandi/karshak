from django.db import models

class bacterialdiseases(models.Model):
   

    def __str__(self):
        return self.disease

    disease=models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    causative_agent=models.CharField(max_length=10000)
    hosts=models.CharField(max_length=1000)
    symptoms=models.CharField(max_length=1000)
    pesticides=models.CharField(max_length=1000)
class fungaldiseases(models.Model):
   

    def __str__(self):
        return self.disease

    disease=models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    causative_agent=models.CharField(max_length=10000)
    hosts=models.CharField(max_length=1000)
    symptoms=models.CharField(max_length=1000)
    pesticides=models.CharField(max_length=1000)
class farmer(models.Model):
    def __str__(self):
        return self.farmerid
    farmerid=models.CharField(max_length=12)
    Name=models.CharField(max_length=100)
    farmland=models.IntegerField()
    phone_no=models.CharField(max_length=10)
class crops(models.Model):
    crop_id=models.IntegerField()
    crop_name=models.CharField(max_length=50)
    crop_year=models.IntegerField()
    cr_ex=models.DecimalField(decimal_places=8,max_digits=10)
    crop_season=models.CharField(max_length=50)
class pesticides(models.Model):
    crop_id =models.IntegerField()
    fert_or_pest=models.CharField( max_length=100)
    price=models.IntegerField()
    fertizer_for=models.CharField( max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)




