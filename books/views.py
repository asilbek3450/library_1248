from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookListSerializer
# Create your views here.


# CBV - class based views
# abstraction, inheritance, polymorphism, encapsulation
# abstraksiya, merosxorlik, polimorfizm, inkapsulyatsiya

class BookListView(ListAPIView):
    queryset = Book.objects.all()  # type: list
    serializer_class = BookListSerializer

