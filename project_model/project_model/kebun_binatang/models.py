from django.db import models
from django.utils import timezone 

# Create your models here.
class Hewan(models.Model):
    nama = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    berat = models.CharField(max_length=25)
    umur = models.CharField(max_length=25)

    def __str__(self):
        return self.nama


class Kandang(models.Model):
    nama = models.CharField(max_length=255)
    isi_kandang = models.TextField(max_length=255)
    luas_kandang = models.CharField(max_length=25)

    def __str__(self):
        return self.nama


class Penjaga(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.TextField(max_length=25)
    jadwal_jaga = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nama


class Pengunjung(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.TextField(max_length=25)
    hari_berkunjung = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nama