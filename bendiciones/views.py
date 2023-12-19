from django.shortcuts import render
from .models import Salud
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def inicio(request):
    # Aquí puedes cargar tu biografía y la foto
    return render(request, 'index.html')

def ejercicios(request):
    data = Salud.objects.all().order_by('-date')

    youtube_salud = data.filter(url__icontains='youtube.com').filter(tipo='EJERCICIO')
    paginator_youtube = Paginator(youtube_salud, 3)
    page_youtube = request.GET.get('page_youtube', 1)

    try:
        data_youtube = paginator_youtube.page(page_youtube)
    except PageNotAnInteger:
        data_youtube = paginator_youtube.page(1)
    except EmptyPage:
        data_youtube = paginator_youtube.page(paginator_youtube.num_pages)

    tiktok_salud = data.filter(url__icontains='tiktok.com')
    paginator_tiktok = Paginator(tiktok_salud, 4)
    page_tiktok = request.GET.get('page_tiktok', 1)

    try:
        data_tiktok = paginator_tiktok.page(page_tiktok)
    except PageNotAnInteger:
        data_tiktok = paginator_tiktok.page(1)
    except EmptyPage:
        data_tiktok = paginator_tiktok.page(paginator_tiktok.num_pages)

    return render(request, 'ejercicios.html',  {'data_youtube': data_youtube, 'data_tiktok': data_tiktok})

def nutricion(request):
    data = Salud.objects.all().order_by('-date').filter(tipo='NUTRICION')

    youtube_salud = data.filter(url__icontains='youtube.com')
    paginator_youtube = Paginator(youtube_salud, 3)
    page_youtube = request.GET.get('page_youtube', 1)

    try:
        data_youtube = paginator_youtube.page(page_youtube)
    except PageNotAnInteger:
        data_youtube = paginator_youtube.page(1)
    except EmptyPage:
        data_youtube = paginator_youtube.page(paginator_youtube.num_pages)

    tiktok_salud = data.filter(url__icontains='tiktok.com')
    paginator_tiktok = Paginator(tiktok_salud, 4)
    page_tiktok = request.GET.get('page_tiktok', 1)

    try:
        data_tiktok = paginator_tiktok.page(page_tiktok)
    except PageNotAnInteger:
        data_tiktok = paginator_tiktok.page(1)
    except EmptyPage:
        data_tiktok = paginator_tiktok.page(paginator_tiktok.num_pages)

    return render(request, 'nutricion.html',  {'data_youtube': data_youtube, 'data_tiktok': data_tiktok})

def card2(request):
    return render(request, 'card2.html')

def card3(request):
    return render(request, 'card3.html')

def card4(request):
    return render(request, 'card4.html')