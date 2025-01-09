from django.db import models
from django.contrib.auth.models import User

# Book Model (for the books available to borrow)
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# BorrowRequest Model (for storing borrow requests)
class BorrowRequest(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')],
        default='pending',
        max_length=10  # Specify the max_length here
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request for {self.book.title} by {self.borrower.username}"

# Profile Model (for user profiles, including bio and picture)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.user.username} at {self.timestamp}"
