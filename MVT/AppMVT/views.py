
from django.http import HttpResponse
from django.shortcuts import render

from django.template import Template, context # importar template u context
from django.template import loader # importar el cargador


from AppMVT.models import Familiar

# Create your views here.

def familia(request):

    template = loader.get_template('template1.html')

    familiar1= Familiar(nombre="Robert", parentesco="Papa", fechadenacimiento="1950-1-1", edad =60, jubilado=1)
    familiar2= Familiar(nombre="Silvana", parentesco="mama", fechadenacimiento="1960-2-2", edad =50, jubilado=1)
    familiar3= Familiar(nombre="Angel", parentesco="Hermano", fechadenacimiento="1970-10-10", edad =40, jubilado=0)
    familiar4= Familiar(nombre="Gustavo", parentesco="Hermano", fechadenacimiento="1980-11-11", edad =30, jubilado=0)

    familiar1.save()
    familiar2.save()
    familiar3.save()
    familiar4.save()

    listadofamiliares = {
        "familiar1": familiar1,
        "familiar2": familiar2,
        "familiar3": familiar3,
        "familiar4": familiar4,
    }

    doc= template.render (listadofamiliares)

    return HttpResponse(doc)