from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Represents a category of products."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Represents a product."""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name="products"
    )
    stock_quantity = models.PositiveIntegerField(default=0)
    image_url = models.URLField(max_length=300, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def average_rating(self):
        """Calculate the average rating for the product."""
        reviews = self.reviews.all()  # Access related reviews via `related_name`
        return reviews.aggregate(models.Avg('rating'))['rating__avg'] or 0

    def review_count(self):
        """Count the number of reviews for the product."""
        return self.reviews.count()


class UserProfile(models.Model):
    """Represents a user profile."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Review(models.Model):
    """Represents a review for a product."""
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'  # Allows reverse lookup from Product to Review
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'  # Allows reverse lookup from User to Review
    )
    rating = models.PositiveIntegerField()  # Rating out of 5 or 10
    comment = models.TextField(blank=True, null=True)  # Optional comment
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review for {self.product.name} by {self.user.username}'
