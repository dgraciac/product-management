from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    # ex: /products/
    path("", views.index, name="index"),
    # ex: /products/5/
    path("<int:product_id>/", views.detail, name="detail"),
    # ex: /products/5/results/
    path("<int:product_id>/results/", views.results, name="results"),
    # ex: /products/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]