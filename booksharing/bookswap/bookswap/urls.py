# bookswap/urls.py
from django.contrib import admin
from django.urls import path
from swap import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    # <-- Ensure there's nothing related to 'share_book' here!
]
