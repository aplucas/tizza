from django.contrib import admin
from django.urls import include, path

from user.views import SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pizzas/', include('pizza.urls')),
    path('register/', SignupView.as_view()),
]

