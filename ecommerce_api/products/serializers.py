from rest_framework import serializers 
from .models import Product, Category, Review


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model."""
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for Review model."""
    user = serializers.StringRelatedField(read_only=True)  # Show username instead of user ID

    class Meta:
        model = Review
        fields = ['id', 'product', 'user', 'rating', 'comment', 'created_at', 'updated_at']
        read_only_fields = ('user', 'created_at', 'updated_at')

    def validate(self, data):
        # Prevent users from reviewing the same product more than once
        user = self.context['request'].user
        product = data['product']
        if Review.objects.filter(user=user, product=product).exists():
            raise serializers.ValidationError("You have already reviewed this product.")
        return data


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model."""
    category = CategorySerializer(read_only=True)  # Display category details
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    reviews = ReviewSerializer(many=True, read_only=True)  # Nested reviews

    class Meta:
        model = Product
        fields = (
            'id', 
            'name', 
            'description', 
            'price', 
            'stock_quantity', 
            'category', 
            'category_id', 
            'created_date', 
            'image_url', 
            'reviews',  # Include reviews in product data
        )
