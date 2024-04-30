from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Position



# Create your views here.


def main_page(request):
    return render(request,"index2.html")

def main_page(request):
    return render(request,"index2.html")


def List_Pos(request):
	position_list = Position.objects.all()
	return render(request,"index2.html",{"position_list": position_list})
