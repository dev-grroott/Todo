from django.urls import path, include

from task.views import home, create_task

urlpatterns = [
    path('', home, name='home'),
    path('create-task', create_task, name="create_task")
]