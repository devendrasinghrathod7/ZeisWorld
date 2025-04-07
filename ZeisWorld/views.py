from django.shortcuts import render
from app.models import Categories,News

from .forms import Students

def home (request):
    category = Categories.objects.all()
    allnews = News.objects.all()
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
        'categories': category,
        'allnews':allnews,
        'topNews':topNews,
        "title":"ZeisWorld | Home"
    }
   
    return render(request, 'index.html',context )

def Trump (request):
    category = Categories.objects.all()
    Trump = News.objects.filter(category__title='Trump').order_by('-id')
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
        'categories': category,
        'Trump':Trump,
        'topNews':topNews,
        "title":"ZeisWorld | Trump"
    }
   
    return render(request, 'categories/Trump.html',context )

def American (request):
    category = Categories.objects.all()
    American = News.objects.filter(category__title='American')
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
        'categories': category,
        'American':American,
        'topNews':topNews,
        "title":"ZeisWorld | American"
    }
   
    return render(request, 'categories/American.html',context )


def Republican (request):
    category = Categories.objects.all()
    Republican = News.objects.filter(category__title='Republican')
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
        'categories': category,
        'Republican':Republican,
        'topNews':topNews,
        "title":"ZeisWorld | Republican"
    }
   
    return render(request, 'categories/Republican.html',context )

def details (request, id):
    news= News.objects.get(pk = id)
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
        'news':news,
        'topNews':topNews,
        "title":"ZeisWorld | Details"
    }
   
    return render(request, 'details.html',context )



def search(request):
    query = request.GET.get('search')
    data = News.objects.filter(title__icontains = query)
    context = {
        'news':data
    }
    return render(request, 'categories/search.html', context)

def studentView(request):
    sf = Students()
    return render(request, 'form.html',{'fm':sf})

def about (request):
    return render(request, 'about.html',{"title":"ZeisWorld | about"})

def contect (request):
    return render(request, 'contect.html',{"title":"ZeisWorld | contect"})


def services (request):
    return render(request, 'services.html',{"title":"ZeisWorld | services"})


def Trending (request):
    return render(request, 'Trending.html',{"title":"ZeisWorld | Trending"})


def Sport (request):
    return render(request, 'Sport.html',{"title":"ZeisWorld | Sport"})


def International (request):
    return render(request, 'International.html',{"title":"ZeisWorld | International"})