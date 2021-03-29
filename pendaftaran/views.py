from django.shortcuts import render, redirect
from . models import Pendaftaran
from datetime import datetime

def daftar(request):
    return render(request, 'daftar/pendaftaran.html')

def tambahdaftar(request):
    if request.method == 'POST':
        nama = request.POST['nama']
        noktp = request.POST['noktp']
        email = request.POST['email']
        telepon = request.POST['telepon']
        tempat_lahir = request.POST['tempat_lahir']
        tanggal_lahir = request.POST['tanggal_lahir']
        goldarah = request.POST['goldarah']
        jenisKelamin = request.POST['jeniskelamin']
        provinsi = request.POST['provinsi']
        kabupaten =request.POST['kabupaten']
        kecamatan = request.POST['kecamatan']
        kelurahan = request.POST['kelurahan']
        domisili = request.POST['domisili']
        alamat_ktp = request.POST['alamat_ktp']
        rt = request.POST['rt']
        rw = request.POST['rw']
        agama = request.POST['agama']
        status_nikah = request.POST['status_nikah']
        profesi = request.POST['profesi']
        pendidikan = request.POST['pendidikan']
        foto1 = request.FILES['foto1']
        foto2 = request.FILES['foto2']
        kesediaan = request.POST['kesediaan']
        w1 = datetime.datetime.now()
        waktu_daftar = w1.strftime("%d/%m/%Y jam %H:%M:%S")
        data = Pendaftaran(
            nama = nama,
            noktp = noktp,
            email = email,
            telepon = telepon,
            tempat_lahir = tempat_lahir,
            tanggal_lahir = tanggal_lahir,
            goldarah = goldarah,
            jenisKelamin = jenisKelamin,
            provinsi = provinsi,
            kabupaten = kabupaten,
            kecamatan = kecamatan,
            kelurahan = kelurahan,
            domisili = domisili,
            alamat_ktp = alamat_ktp,
            rt = rt,
            rw = rw,
            agama = agama,
            status_nikah = status_nikah,
            profesi = profesi,
            pendidikan = pendidikan,
            foto1 = foto1,
            foto2 = foto2,
            kesediaan = kesediaan,
            waktu_daftar = waktu_daftar
        )
        data.save()
        return redirect('daftar')

        