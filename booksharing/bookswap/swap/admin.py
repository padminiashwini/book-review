from django.contrib import admin
from .models import Book, Review

# Register Book and Review models
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'average_rating', 'is_available')
    search_fields = ('title', 'author')
    list_filter = ('is_available',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user_name', 'rating', 'review_text')
    search_fields = ('user_name', 'book__title')
    list_filter = ('rating',)
