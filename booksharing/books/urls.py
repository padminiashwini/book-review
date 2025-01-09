from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('chat/<int:borrow_request_id>/', views.chat, name='chat'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
]

