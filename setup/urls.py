
from django.contrib import admin
from django.urls import path
from todos.views import home
from todos.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', home),
    path('login/', login),
]
