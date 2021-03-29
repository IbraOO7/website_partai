from django.shortcuts import get_object_or_404, render, redirect
from blog.models import Berita
from django.views.generic.list import ListView

class IndexView(ListView):
    queryset = Berita.objects.all().order_by("-id")
    template_name = "index.html"
    context_object_name = "berita"
    paginate_by = 3

def isinya(request, no_berita):
   list = get_object_or_404(Berita, pk=no_berita)
   list2 = Berita.objects.all().order_by("-id")[:3]
   context = {"list":list, "list2": list2}
   return render(request, 'isi1/isinya.html', context)

def tentang(request):
    return render(request, 'isi1/tentang.html')

def blog(request):
    return render(request, 'isi1/blog.html')