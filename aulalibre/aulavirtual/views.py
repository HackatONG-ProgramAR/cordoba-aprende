from django.shortcuts import render
from django.http import HttpResponse
from aulavirtual.models import Recurso

# Create your views here.

def alumno(request):
    recursos =  Recurso.objects.order_by('id')[:10]
    return render(request, 'libros.html', {'recursos': recursos})
