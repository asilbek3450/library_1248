from django.urls import path, include
# from .views import BookListView, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView
from .views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView

urlpatterns = [
    # path('books', BookListView.as_view()),
    # path('create/', BookCreateView.as_view()),
    # path('<int:pk>/', BookDetailView.as_view()),
    # path('update/<int:pk>/', BookUpdateView.as_view()),
    # path('delete/<int:pk>/', BookDeleteView.as_view()),

    path('bookscreate/', BookListCreateAPIView.as_view()),
    path('booksignle/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view()),


]
