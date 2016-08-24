from django.http import Http404
from django.shortcuts import render

# Create your views here.

from .models import Product

# def detail_view(request, object_id=None):
# 	product = get_object_or_404(Product, id=object_id)
# 	template = "detail_view.html"