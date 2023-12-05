from django.db import models

# Create your models here.
from django.db import models
import datetime

from django.db import models
from django.utils import timezone


class Sual(models.Model):
    sual_metni= models.CharField(max_length=200)
    qeydiyyat_tarixi = models.DateTimeField("gorunen tarix")
    def __str__(self):
        return self.sual_metni
    def __str__(self):
        return self.secim_metni
    def en_yeni_elave(self):
        return self.qeydiyyat_tarixi >= timezone.now() - datetime.timedelta(days=1)
class Secim(models.Model):
    sual = models.ForeignKey(Sual, on_delete=models.CASCADE)
    secim_metni = models.CharField(max_length=200)
    sesler = models.IntegerField(default=0)
    def __str__(self):
        return self.secim_metni