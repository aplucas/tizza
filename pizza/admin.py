from django.contrib import admin

from pizza.models import Pizza, Pizzeria


class PizzaAdmin(admin.ModelAdmin):
    pass


class PizzeriaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Pizzeria, PizzeriaAdmin)
