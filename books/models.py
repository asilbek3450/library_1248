from django.db import models


# Create your models here.
class Author(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # FK
    image = models.ImageField(upload_to='books_images/', null=True, blank=True)
    description = models.TextField()  # kitob haqida ma'lumot
    price = models.PositiveIntegerField()
    published_date = models.DateField(auto_now_add=True)

    isbn = models.CharField(max_length=13)
    pages = models.PositiveIntegerField()

    def __str__(self):
        return self.title
