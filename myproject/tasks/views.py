from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

# Список тасків + створення нового
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Перегляд, оновлення та видалення конкретного таску
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
