from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView
from user.views import SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pizzas/', include('pizza.urls')),
    path('register/', SignupView.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]
