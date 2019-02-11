from django.db import models
from django.utils import timezone 

# Create your models here.
class Direksi(models.Model):
    nama_lengkap = models.TextField(max_length=255)
    no_telepon = models.CharField(max_length=25)
    jabatan = models.CharField(max_length=25)
    umur = models.CharField(max_length=25)

    def __str__(self):
        return self.nama_lengkap


class Mentee(models.Model):
    nama_lengkap = models.TextField(max_length=255)
    no_telepon = models.CharField(max_length=25)
    nomor_absen = models.CharField(max_length=25)
    nilai_rata_rata = models.CharField(max_length=25)

    def __str__(self):
        return self.nama_lengkap


class Mata_pelajaran(models.Model):
    nama_pelajaran = models.TextField(max_length=255)
    jadwal_dimulai = models.DateTimeField(default=timezone.now)
    jadwal_berakhir = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nama_pelajaran


class Mentor(models.Model):
    nama_lengkap = models.TextField(max_length=255)
    no_telepon = models.CharField(max_length=25)
    mata_pelajaran = models.ForeignKey(Mata_pelajaran, on_delete=models.CASCADE)
    nilai_rata_rata = models.CharField(max_length=25)

    def __str__(self):
        return self.nama_lengkap


class Challenge(models.Model):
    nama_challenge = models.TextField(max_length=255)
    banyak_soal = models.CharField(max_length=25)
    bobot_nilai = models.CharField(max_length=25)
    mata_pelajaran = models.ForeignKey(Mata_pelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_challenge


class Live_code(models.Model):
    nama_live_code = models.TextField(max_length=255)
    banyak_soal = models.CharField(max_length=25)
    bobot_nilai = models.CharField(max_length=25)
    tanggal_pelaksanaan = models.DateTimeField(default=timezone.now)
    mata_pelajaran = models.ForeignKey(Mata_pelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_live_code