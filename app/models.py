from django.db import models

# Create your models here.
class School(models.Model):
    code = models.CharField(max_length=10, blank=True)
    label = models.CharField(max_length=200)
    post_box = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.label

class Study(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    serial_number = models.CharField(max_length=20, help_text="Entrez un matricule sous le format 00A0000AA")
    #school = models.CharField(max_length=60)
    code = models.CharField(max_length=10, blank=True)
    label = models.CharField(max_length=200)
    post_box = models.CharField(max_length=10, blank=True)

    #school = models.ManyToManyField(School, related_name='studies')

    def __str__(self):
        return self.first_name

    def __unicode__(self):
        return 


class Frequenter(models.Model):
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.study, self.school)

    def __unicode__(self):
        return 
