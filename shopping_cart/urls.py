# urls.py
from django.urls import path
from .views import UserListCreate, UserRetrieveUpdateDestroy, ProductListCreate, ProductRetrieveUpdateDestroy, \
    OrderListCreate, OrderRetrieveUpdateDestroy, PaymentListCreate, PaymentRetrieveUpdateDestroy, OrderItemCreate

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-retrieve-update-destroy'),
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-retrieve-update-destroy'),
    path('orders/', OrderListCreate.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroy.as_view(), name='order-retrieve-update-destroy'),
    path('orderitems/', OrderItemCreate.as_view(), name='order-item-create'),
    path('payments/', PaymentListCreate.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentRetrieveUpdateDestroy.as_view(), name='payment-retrieve-update-destroy'),

    # JWT URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Endpoint for obtaining tokens
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Endpoint for refreshing tokens
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # Endpoint for verifying tokens

]
