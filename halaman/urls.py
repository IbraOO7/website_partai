from halaman.views import tentang
from django.urls import path
from . views import IndexView, isinya

from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('isinya/<int:no_berita>', views.isinya, name='isinya'),
    path('tentang/', views.tentang, name='tentang'),
    path('blog/', views.blog, name='blog')
]
