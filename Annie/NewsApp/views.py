from django.shortcuts import render
# from django.shortcuts import HttpResponse
from .models import News


# Create your views here.
def Home(request):
    context = {
        "name": "Ama"
    }
    return render(request, "home.html", context)


def NewsP(request):
    obj = News.objects.get(id=1)

    context = {
        "data": obj
    }
    # return HttpResponse("<h1>This is our latest news</h1>")
    return render(request, "news.html", context)


def NewsDate(request, year):
    article_list = News.objects.filter(date_published__year=year)
    context = {
        'year': year,
        'article_list': article_list
    }

    return render(request, "newsdate.html", context)


def Contact(request):
    return render(request, "contact.html")
