from django.core.cache import cache
from django.shortcuts import render


# Create your views here.
def index(request):
    all_rows = cache.get_many(cache.keys("*"))
    context = {"all_rows": all_rows}
    return render(request, 'web/index.html', context=context)
