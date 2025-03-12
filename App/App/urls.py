from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('task_list/', task_list, name="task_list"),
    path('task_create/', task_create, name="task_create"),
    path('task_update/<int:pk>/', task_update, name="task_update"),
    path('task_delete/<int:pk>/', task_delete, name="task_delete"),
]
