from django.db import models

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=30)
    type = models.ForeignKey(Type,on_delete=models.CASCADE)
    client = models.CharField(max_length=30)
    date = models.DateField()
    url = models.CharField(max_length=100)
    text = models.TextField()
    picture1 = models.ImageField(upload_to='media')
    picture2 = models.ImageField(upload_to='media',null=True,blank=True)
    picture3 = models.ImageField(upload_to='media',null=True,blank=True)

class Position(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=30)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    text = models.TextField()
    picture1 = models.ImageField(upload_to='media')
    picture2 = models.URLField('media',null=True,blank=True)
    picture3 = models.URLField('media',null=True,blank=True)
    picture4 = models.URLField('media', null=True, blank=True)
    picture5 = models.URLField('media', null=True, blank=True)


class Services(models.Model):
    name = models.CharField(max_length=40)
    text = models.TextField()
    picture1 = models.ImageField(upload_to='media')


class Contact(models.Model):
    name = models.CharField(max_length=40)
    gmail = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField()

class Subscribe(models.Model):
    gmail = models.EmailField(max_length=50)