# serializer
from rest_framework import serializers
from .models import Book, Author


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = ['id', 'title', 'author', 'price', 'published_date']

    def validate(self, attrs):
        title = attrs.get('title', None)
        isbn = attrs.get('isbn', None)
        price = attrs.get('price', None)
        pages = attrs.get('pages', None)

        if Book.objects.filter(title=title).exists():
            raise serializers.ValidationError(
                {
                    'status': False,
                    'message': 'Bunday kitob mavjud'
                }
            )

        if Book.objects.filter(isbn=isbn).exists():
            raise serializers.ValidationError(
                {
                    'status': False,
                    'message': 'Bunday isbnli kitob mavjud'
                }
            )

        if not 0 < price < 10000000:
            raise serializers.ValidationError(
                {
                    'status': False,
                    'message': 'Narx 0 dan 10000000 gacha bo\'lishi kerak'
                }
            )

        if pages < 0:
            raise serializers.ValidationError(
                {
                    'status': False,
                    'message': 'Sahifa 0 dan katta bo\'lishi kerak'
                }
            )
        return attrs


# ModelSerializer vs Serializer
# ModelSerializer - avtomatik ravishda modelni tanib, fieldlarni tuzib beradi
# Serializer - fieldlarni ozimiz tuzib beramiz

# serializers.Serializer
# serializers.ModelSerializer


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'full_name', 'age', 'email', 'phone']

    # Validation and Field-level validation

    def validate(self, attrs):
        full_name = attrs.get('full_name', None)
        phone = attrs.get('phone', None)

        if Author.objects.filter(full_name=full_name).exists():
            raise serializers.ValidationError(
                {
                    'status': False,
                    'message': 'Bunday avtor mavjud, yana yaratib bo\'lmaydi'
                }
            )

        if not full_name.isalpha():
            raise serializers.ValidationError(
                {
                    'status': False,
                    'message': 'Ism familiya harfdan iborat bo\'lishi kerak'
                }
            )
        if len(phone) != 13:
            raise serializers.ValidationError(
                {
                    'status': False,
                    'message': 'Telefon raqami 13 ta belgidan iborat bo\'lishi kerak'
                }
            )
        return attrs

    def validate_age(self, age):
        if age < 6:
            raise serializers.ValidationError('Avtor yoshi 6 dan kam bo\'lishi mumkin emas')
        return age

    def validate_email(self, email):
        if not email.endswith('@gmail.com'):
            raise serializers.ValidationError('Emailni gmail.com domaini bilan tugatilishi kerak')
        return email


# class AuthorDetailSerializer(serializers.Serializer):
#     full_name = serializers.CharField()
#     age = serializers.IntegerField()
#     email = serializers.EmailField()
#     phone = serializers.CharField()
#
#     def create(self, validated_data):
#         return Author.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.full_name = validated_data.get('full_name', instance.full_name)
#         instance.age = validated_data.get('age', instance.age)
#         instance.email = validated_data.get('email', instance.email)
#         instance.phone = validated_data.get('phone', instance.phone)
#         instance.save()
#         return instance

