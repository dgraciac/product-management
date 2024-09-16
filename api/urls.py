from django.urls import path
from .views import UserView, UpdateDeleteUserView, ProductView, GetUpdateDeleteProductView
from . import views

app_name = 'api'
urlpatterns = [
    path('users', UserView.as_view(), name='users'),
    path('users/<int:pk>', UpdateDeleteUserView.as_view(), name='update-delete-user'),
    path("products", ProductView.as_view(), name="products"),
    path('products/<int:pk>', GetUpdateDeleteProductView.as_view(), name='update-delete-product'),
]
