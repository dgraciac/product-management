from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from .models import Product

from oauth2_provider.decorators import protected_resource

@protected_resource()
def index(request):
    products = Product.objects.all()
    output = ", ".join([product.name for product in products])
    return HttpResponse(output)

def detail(request, product_id):
    question = get_object_or_404(Product, pk=product_id)
    return question


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)