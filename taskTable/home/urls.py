from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('sort-table/<slug:col><int:asec>',views.homepage,name='sort_table'),
    path('create-task',views.create_task,name='create_task'),
    path(r'delete-task/<int:id>',views.delete_task,name='delete_task'),
    path(r'update-statue/<int:id><',views.update_status,name='update_status'),
]
