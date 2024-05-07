from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Book
from .serializers import BookListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


# CBV - class based views
# abstraction, inheritance, polymorphism, encapsulation
# abstraksiya, merosxorlik, polimorfizm, inkapsulyatsiya

# class BookListView(ListAPIView):  # get
#     queryset = Book.objects.all()  # type: list
#     serializer_class = BookListSerializer
#
#
# class BookCreateView(CreateAPIView):  # post
#     queryset = Book.objects.all()
#     serializer_class = BookListSerializer
#
#
# class BookDetailView(RetrieveAPIView):  # get
#     queryset = Book.objects.all()
#     serializer_class = BookListSerializer
#
#
# class BookUpdateView(UpdateAPIView):  # put, patch
#     queryset = Book.objects.all()
#     serializer_class = BookListSerializer
#
#
# class BookDeleteView(DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookListSerializer
#
#
# class BookListCreateAPIView(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookListSerializer
#
#
# class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):  # get, put, patch, delete
#     queryset = Book.objects.all()
#     serializer_class = BookListSerializer


# CRUD - Create, Retrieve(Read), Update, Delete

# concrete views
# 1. ListAPIView
# 2. CreateAPIView
# 3. RetrieveAPIView
# 4. UpdateAPIView
# 5. DestroyAPIView
# 6. ListCreateAPIView
# 7. RetrieveUpdateDestroyAPIView

# class based views
# 1. APIView
# 2. ModelViewSet
# 3. GenericAPIView
# 4. ViewSet
# 5. GenericViewSet
# 6. ReadOnlyModelViewSet


class BookList(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        data = {
            'status': f"{len(books)} ta kitob mavjud",
            'kitoblar': serializer.data
        }
        return Response(data)

    def post(self, request):
        data = request.data
        serializer = BookListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': 'Kitob muvaffaqiyatli yaratildi',
                'kitob': serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def patch(self, request, pk):
        pass

    def delete(self, request, pk):
        pass

