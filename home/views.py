from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import HttpResponse
from home.models import Books

# Create your views here.


def Index(request):
    all_bokks = Books.objects.all()
    paginator = Paginator(all_bokks,3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'page':page
    }
    return render(request,'book_list.html',context)
