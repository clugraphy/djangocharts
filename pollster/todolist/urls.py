from django.urls import path
from . import views


app_name = 'todolist'
urlpatterns = [
    path('', views.todolist, name = 'todolist'),
    # path('todolist',views.todolist, name=''),
    path('detele/<task_id>', views.delete_task, name = 'delete_task'),
    path('edit/<task_id>', views.edit_task, name = 'edit_task'),
    path('complete/<task_id>', views.complete_task, name = 'complete_task'),
    path('pending/<task_id>', views.pending_task, name = 'pending_task'),

]
