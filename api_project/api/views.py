from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Book

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    ["generics.ListAPIView"]



class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    ["viewsets.ModelViewSet"]
