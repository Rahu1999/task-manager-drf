from django.shortcuts import get_object_or_404
from .models import TaskList,Task
from .serializers import TaskListSerializer,TaskSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
import json

# Create your views here.


class TaskManager(viewsets.ViewSet):
    
    def get_all_task_list(self,request):
        taskList = TaskList.objects.all()
        serializer = TaskListSerializer(taskList, many= True)
        return Response(serializer.data)
    
    def add_task_list(self,request):
        data = json.loads(request.body)
        serializer = TaskListSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update_task_list(self,request,task_list_id):
        data = json.loads(request.body)
        taskList = get_object_or_404(TaskList, id=task_list_id)
        serializer = TaskListSerializer(taskList,data= data,partial=True)# if we remove partial= True required all data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete_task_list(self,request,task_list_id):
        taskList = get_object_or_404(TaskList, id=task_list_id)
        taskList.delete()
        return Response({'message': 'TaskList deleted successfully'}, status=status.HTTP_204_NO_CONTENT)