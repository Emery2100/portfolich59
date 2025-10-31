from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=30)


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    year = models.IntegerField()
    image = models.ImageField(upload_to='project/')
    repository = models.URLField(max_length=200)
    skills = models.ManyToManyField('Skill')
