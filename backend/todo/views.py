from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import TodoSerializer
from .models import Todo
from rest_framework.decorators import api_view
from django.shortcuts import render

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class Tutorial(object):
    pass


@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    def tutorial_detail(request, pk):
        # find tutorial by pk (id)
        try:
            tutorial = Tutorial.objects.get(pk=pk)
        except Tutorial.DoesNotExist:
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 



