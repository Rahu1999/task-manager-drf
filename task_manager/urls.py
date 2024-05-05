from django.contrib import admin
from django.urls import path
from api.views import TaskManager

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task-list/',TaskManager.as_view({'get':'get_all_task_list','post':'add_task_list'})),
    path('task-list/<int:task_list_id>',TaskManager.as_view({'put':'update_task_list','delete':'delete_task_list'}))
]
