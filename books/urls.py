from django.urls import path, include
# from .views import BookListView, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView
# from .views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView
from .views import BookList, BookDetail, AuthorList, AuthorDetail

urlpatterns = [

    # path('books/', BookListView.as_view()),
    # path('books/create/', BookCreateView.as_view()),
    # path('books/<int:pk>/', BookDetailView.as_view()),
    # path('books/update/<int:pk>/', BookUpdateView.as_view()),
    # path('books/delete/<int:pk>/', BookDeleteView.as_view()),
    #
    # path('bookscreate/', BookListCreateAPIView.as_view()),
    # path('booksignle/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view()),

    path('books/', BookList.as_view()),
    path('books/<int:pk>/', BookDetail.as_view()),

    path('authors/', AuthorList.as_view()),
    path('authors/<int:pk>/', AuthorDetail.as_view()),
]
