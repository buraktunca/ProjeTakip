from django.db import models
import random
# Create your models here.
DONORS = [
    ('ALMAN KIZILHAÇI', 'ALMAN KIZILHAÇI'),
    ('NORVEÇ KIZILHAÇI', 'NORVEÇ KIZILHAÇI'),
    ('KATAR KIZILHAÇI', 'KATAR KIZILHAÇI'),
]
ROLES = [
    ('Staff', 'Staff'),
    ('ProjectManager', 'ProjectManager'),
    ('Manager', 'Manager'),
]
CC = [
    ('Adana Toplum Merkezi', 'Adana Toplum Merkezi'),
    ('Ankara Toplum Merkezi', 'Ankara Toplum Merkezi'),
    ('Mersin Toplum Merkezi', 'Mersin Toplum Merkezi'),
    ('Merkez Ofis', 'Merkez Ofis'),
    ]

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=False)
    project_start = models.DateField(auto_now=False, auto_now_add=False)
    project_finish =models.DateField(auto_now=False, auto_now_add=False)
    project_budget = models.DecimalField(max_digits=25, decimal_places=2)
    project_donor = models.CharField(max_length=100, choices=DONORS,default="ALMAN KIZILHAÇI")
    def __str__(self):
        return self.project_name

class Person(models.Model):
    name = models.CharField(max_length=200)
    surname =  models.CharField(max_length=200)
    email = models.EmailField(max_length=254,unique=True)
    password = models.CharField(max_length=200)
    tm = models.CharField(max_length=100, choices=CC,default="Merkez Ofis")
    def __str__(self):
        return self.email

class autority(models.Model):
    proje=models.ForeignKey("Project",on_delete=models.CASCADE)
    person=models.ForeignKey("Person",on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=ROLES)
    tm = models.CharField(max_length=100, choices=CC)

class indic(models.Model):
    proje=models.ForeignKey("Project",on_delete=models.CASCADE)
    indikator_name=models.CharField(max_length=200)
    indikator_detail =models.CharField(max_length=1000)
    indikator_hedef = models.IntegerField()
    class Meta:
        unique_together = [['proje', 'indikator_name']]
