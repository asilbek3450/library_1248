from django.db import models


# Create your models here.
class Author(models.Model):
    pass


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)  # FK
    image = models.ImageField(upload_to='books_images/', null=True, blank=True)
    description = models.TextField()  # kitob haqida ma'lumot
    price = models.PositiveIntegerField()
    published_date = models.DateField(auto_now_add=True)

    isbn = models.CharField(max_length=13)
    pages = models.PositiveIntegerField()

    def __str__(self):
        return self.title
