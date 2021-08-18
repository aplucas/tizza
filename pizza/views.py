import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from pizza.models import Pizza


@login_required
def index(request, pid):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_pizza = Pizza.objects.create(
            title=data['title'],
            description=data['description'],
            thumbnail_url=data['thumbnail_url'],
            creator=request.user,
            types=data['types']
        )
        new_pizza.save()
        return JsonResponse(
            content={
                'id': new_pizza.id,
                'title': new_pizza.title,
                'description': new_pizza.description
            }
        )
    elif request.method == 'GET':
        try:
            pizza = Pizza.objects.get(id=pid)
            data = {
                'id': pizza.id,
                "title": pizza.title,
                "description": pizza.description,
                "thumbnail_url": pizza.thumbnail_url,
                "types": pizza.types,
            }
        except Pizza.DoesNotExist as e:
            data = {
                "status": "erro",
                "message": 'pizza não encontrada'
            }
        return JsonResponse(data)


def random(request):
    pizzas = Pizza.objects.exclude(likes__user=request.user).order_by("?")[:15].values()

    return JsonResponse(list(pizzas), safe=False)
