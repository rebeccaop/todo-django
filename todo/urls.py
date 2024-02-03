from django.urls import path
from . import views

urlpatterns = [
  path('add_task/',views.task,name= 'add task'),
  path('mark_as_done/<int:pk>/',views.mark_as_done, name= 'mark as done'),
  path('mark_as_Undon/<int:pk>/',views.mark_as_undone, name= 'mark as Undone'),
  path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),
  path('delete_task/<int:pk>/',views.delete_task,name='delete_task')
]