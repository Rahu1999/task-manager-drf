from django.contrib import admin
from django.urls import path,include
from api.views import TaskListManager

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('api.urls')),
    # path('task-list/',TaskListManager.as_view({'get':'get_all_task_list','post':'add_task_list'})),
    # path('task-list/<int:task_list_id>',TaskListManager.as_view({'put':'update_task_list','delete':'delete_task_list'}))
]
