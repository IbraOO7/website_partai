from django.contrib import admin
from . models import Pendaftaran

class AdminPendaftaran(admin.ModelAdmin):
    list_display = ('id','nama','noktp','tempat_lahir','tanggal_lahir','jenisKelamin','telepon','email')
    list_display_links = ('id','nama')
    search_fields = ('nama','email','telepon')
    list_per_page = 25

admin.site.register(Pendaftaran, AdminPendaftaran)
