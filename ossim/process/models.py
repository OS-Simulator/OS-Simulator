from django.db import models

# Create your models here.

class ProcessSchedAlg(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()
    demourl = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Adv(models.Model):
    alg = models.ForeignKey(ProcessSchedAlg, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)


    def __str__(self):
        return self.text
