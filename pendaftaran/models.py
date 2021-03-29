from django.db import models

class Pendaftaran(models.Model):
    nama = models.CharField(max_length=200)
    noktp = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    telepon = models.CharField(max_length=100)
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.CharField(max_length=80)
    goldarah = models.CharField(max_length=20)
    jenisKelamin = models.CharField(max_length=20)
    provinsi = models.CharField(max_length=100)
    kabupaten = models.CharField(max_length=100)
    kecamatan = models.CharField(max_length=100)
    kelurahan = models.CharField(max_length=100)
    domisili = models.TextField(blank=True)
    alamat_ktp = models.TextField(blank=True)
    rt = models.CharField(max_length=100)
    rw = models.CharField(max_length=100)
    agama = models.CharField(max_length=100)
    status_nikah = models.CharField(max_length=100)
    profesi = models.CharField(max_length=100)
    pendidikan = models.CharField(max_length=100)
    foto1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    kesediaan = models.CharField(max_length=15)
    waktu_daftar = models.CharField(max_length=60)
    
    def __str__(self):
        return self.nama
    
