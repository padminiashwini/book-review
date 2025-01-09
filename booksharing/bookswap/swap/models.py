from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    is_available = models.BooleanField(default=True)  # True if the book is available for sharing
    average_rating = models.FloatField(default=0)  # Field to store average rating

    def __str__(self):
        return self.title

    def update_average_rating(self):
        reviews = self.reviews.all()  # Get all reviews for the book
        if reviews:
            total_rating = sum([review.rating for review in reviews])
            self.average_rating = total_rating / len(reviews)
            self.save()

class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    review_text = models.TextField()
    rating = models.IntegerField(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)])

    def __str__(self):
        return f"Review for {self.book.title} by {self.user_name}"
