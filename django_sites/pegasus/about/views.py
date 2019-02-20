from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'about/index.html')


def brenna(request):
	return render(request, 'about/brenna.html')


def fatma(request):
    return HttpResponse("Fatma's page.")


def wafi(request):
    return HttpResponse("Wafi's page.")


def zachary(request):
    return render(request, 'about/zachary.html')


def adan(request):
    return HttpResponse("Adan's page.")


def quan(request):
    return HttpResponse("Quan's page.")


def omar(request):
    return HttpResponse("Omar's page.")
