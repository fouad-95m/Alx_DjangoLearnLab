from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Category, Review
from .serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from .permissions import IsReviewOwner


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for managing categories."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet for managing products."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'description']
    filterset_fields = ['category', 'price', 'stock_quantity']


class ReviewViewSet(viewsets.ModelViewSet):
    """ViewSet for managing reviews."""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        """Assign permissions dynamically based on action."""
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsReviewOwner()]  # Only the owner can edit/delete
        return [IsAuthenticatedOrReadOnly()]  # Everyone can read; authenticated users can create

    def get_queryset(self):
        """Optionally filter reviews by product."""
        product_id = self.request.query_params.get('product_id')
        if product_id:
            return self.queryset.filter(product__id=product_id)
        return self.queryset

    def perform_create(self, serializer):
        """Automatically associate the logged-in user with the review."""
        serializer.save(user=self.request.user)
