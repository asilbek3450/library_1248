# serializer
from rest_framework import serializers
from .models import Book, Author


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
        # fields = ['id', 'title', 'author', 'price', 'published_date']


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'
