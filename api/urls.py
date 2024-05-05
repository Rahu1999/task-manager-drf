
from django.urls import path
from .views import TaskListManager,TaskManager

urlpatterns = [
    path('task-list/',TaskListManager.as_view({'get':'get_all_task_list','post':'add_task_list'})),
    path('task-list/<int:task_list_id>',TaskListManager.as_view({'put':'update_task_list','delete':'delete_task_list'})),
    path('task/',TaskManager.as_view({'post':'add_task'})),
    path('task/<int:task_list_id>',TaskManager.as_view({'get':'task_by_list_id',})),
    path('task-action/<int:task_id>',TaskManager.as_view({'put':'update_task','delete':'delete_task'})),
]
