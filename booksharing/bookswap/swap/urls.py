from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),  # This is the URL for both listing books and search
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]
