from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Book
from rest_framework.permissions import IsAuthenticated

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    ["generics.ListAPIView"]



class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users
    ["viewsets.ModelViewSet"]

