from django.urls import path
from .views import UserView, UpdateDeleteUserView
from . import views

app_name = 'api'
urlpatterns = [
    path('users', UserView.as_view(), name='users'),
    path('users/<int:pk>', UpdateDeleteUserView.as_view(), name='update-delete-user'),
    # ex: /products/
    path("", views.index, name="index"),
    # ex: /products/5/
    path("<int:product_id>/", views.detail, name="detail"),
    # ex: /products/5/results/
    path("<int:product_id>/results/", views.results, name="results"),
    # ex: /products/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
