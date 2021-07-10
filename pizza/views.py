from django.http import JsonResponse

from .models import Pizza


def index(request, pid):
    try:
        pizza = Pizza.objects.get(id=pid)

        data = {
            "title": pizza.title,
            "description": pizza.description,
            "thumbnail_url": pizza.thumbnail_url,
        }
    except Pizza.DoesNotExist as e:
        data = {
            "status": "erro",
            "message": 'pizza não encontrada'
        }
    return JsonResponse(data)

def random(request):
    pizzas = Pizza.objects.order_by("?")[:15].values()
    
    return JsonResponse(list(pizzas), safe=False)