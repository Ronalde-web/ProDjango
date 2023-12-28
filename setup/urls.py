
from django.contrib import admin
from django.urls import path
from todos.views import home
from todos.views import login
from todos.views import ronalde

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', home),
    path('login/', login),
    path('ronalde/', ronalde),
]
