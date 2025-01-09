from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q  # Import Q for complex queries
from .models import Book, Review

# Home page view
def home(request):
    return render(request, 'swap/home.html')

# View to display all available books or search results
def book_list(request):
    books = Book.objects.filter(is_available=True)  # Only available books

    # Search functionality
    query = request.GET.get('q')  # Get the search query from the URL (GET parameter 'q')
    if query:
        # Using Q to combine multiple search filters in a cleaner way
        books = books.filter(Q(title__icontains=query) | Q(author__icontains=query))

    return render(request, 'swap/book_list.html', {'books': books, 'query': query})

# View to display the details of a specific book and handle reviews
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)  # Use get_object_or_404 for better error handling

    # Handle review submission
    if request.method == 'POST':
        user_name = request.POST.get('user_name', '').strip()
        review_text = request.POST.get('review_text', '').strip()
        rating = int(request.POST.get('rating', 0))

        if user_name and review_text and 1 <= rating <= 5:  # Validate form inputs
            # Create and save the review
            Review.objects.create(book=book, user_name=user_name, review_text=review_text, rating=rating)
            # Update the book's average rating
            book.update_average_rating()  # Ensure this method exists in your Book model
            return redirect('book_detail', book_id=book.id)  # Redirect to avoid duplicate form submission

    # Get all reviews for the book
    reviews = book.reviews.all()

    return render(request, 'swap/book_detail.html', {'book': book, 'reviews': reviews})
