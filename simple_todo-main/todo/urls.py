from django.contrib import admin
from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    # path('admin/', admin.site.urls),
path('', views.todos, name="todos" )

]
