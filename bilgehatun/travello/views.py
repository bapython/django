from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# def index(request):
#     dest1 = Destination()
#     dest1._id = 1
#     dest1.name = 'Bali'
#     dest1.img = 'destination_1.jpg'
#     dest1.description = 'Nulla pretium tincidunt felis, nec.'
#     dest1.price = 600
#     dest1.offer = True

#     dest2 = Destination()
#     dest2._id = 2
#     dest2.name = 'Mali'
#     dest2.img = 'destination_2.jpg'
#     dest2.description = 'Nulla pretium tincidunt felis, nec.'
#     dest2.price = 700
#     dest2.offer = False

#     dest3 = Destination()
#     dest3._id = 3
#     dest3.name = 'Dali'
#     dest3.img = 'destination_3.jpg'
#     dest3.description = 'Nulla pretium tincidunt felis, nec.'
#     dest3.price = 800
#     dest3.offer = True

#     dests = [
#         dest1,dest2,dest3
#     ]

#     return render(request, 'travello/index.html',{'dests':dests})

def index(request):
    dests = Destination.objects.all()

    return render(request, 'travello/index.html',{'dests':dests})