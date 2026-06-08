from django.http import JsonResponse
from .models import Carro

def listar_carros(request):
    carros = Carro.objects.all().values()
    return JsonResponse(list(carros), safe=False)

def listar_carros_disponiveis(request):
    carros = Carro.objects.filter(situacao='disponivel').values()
    return JsonResponse(list(carros), safe=False)

def listar_carros_reservados(request):
    carros = Carro.objects.filter(situacao='reservado').values()
    return JsonResponse(list(carros), safe=False)

def listar_carros_vendidos(request):
    carros = Carro.objects.filter(situacao='vendido').values()
    return JsonResponse(list(carros), safe=False)