from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'categories/index.html')


def create(request):
    return render(request, "categories/create.html")


def add(request):
    categoryName = request.POST['CategoryName']
    description = request.POST['Description']

    return render(request, 'categories/index.html',{  "CategoryID": 1,  "CategoryName": "Beverages", "Description": "Soft drinks, coffees, teas, beers, and ales"  }  )
