from django.shortcuts import render, redirect
from .models import Book, BorrowRequest, Chat, Profile
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

# View to borrow a book (submit borrow request)
@login_required
def borrow_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        borrow_request = BorrowRequest.objects.create(book=book, borrower=request.user)
        return redirect('chat', borrow_request_id=borrow_request.id)
    return render(request, 'borrow_request.html', {'book': book})

# View to handle the chat related to a borrow request
@login_required
def chat(request, borrow_request_id):
    borrow_request = BorrowRequest.objects.get(id=borrow_request_id)
    if request.method == 'POST':
        message = request.POST['message']
        # Create the chat message and link it to the borrow request
        Chat.objects.create(borrow_request=borrow_request, sender=request.user, message=message)
    chats = Chat.objects.filter(borrow_request=borrow_request)
    return render(request, 'chat.html', {'chats': chats, 'borrow_request': borrow_request})

# View for user's profile
@login_required
def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    return render(request, 'profile.html', {'profile': profile})

# View to update user's profile
@login_required
def update_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'update_profile.html', {'form': form})

# books/views.py

# View for the home page (can be used for the root URL)
def home(request):
    books = Book.objects.all()  # List all books available for borrowing
    return render(request, 'home.html', {'books': books})
