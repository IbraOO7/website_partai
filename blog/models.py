from django.db import models
from datetime import datetime

class Berita(models.Model):
    judul = models.CharField(max_length=200)
    isi_berita = models.TextField()
    gambar = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    trending = models.CharField(max_length=80, blank=True)
    waktu_posting = models.DateTimeField(default=datetime.now(), blank=True)
    
    def __str__(self):
        return self.judul
    
    def imageURL(self):
        try:
            url = self.gambar.url
        except:
            url = ''
        return url

class ketuaUmum(models.Model):
    judul = models.CharField(max_length=200)
    isi_berita = models.TextField()
    gambar = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    waktu_posting = models.CharField(max_length=100, blank=True)
    tags = models.TextField()
    
    def __str__(self):
        return self.judul
    
    def imageURL(self):
        try:
            url = self.gambar.url
        except:
            url = ''
        return url

class Artikel(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    gambar = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    waktu_posting = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        self.judul
    
    def imageURL(self):
        try:
            url = self.gambar.url
        except:
            url = ''
        return url