from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
# Create your views here.
from digitalmarket.mixins import MultipleSlugMixin, SubmitBtnMixin
from .forms import ProductAddForm, ProductModelForm
from .models import Product


class ProductCreateView(SubmitBtnMixin, CreateView):
    model = Product
    template_name = 'form.html'
    form_class = ProductModelForm
    success_url = "/products/add"
    submit_btn = 'Add Product'


class ProductUpdateView(SubmitBtnMixin, MultipleSlugMixin, UpdateView):
    model = Product
    template_name = 'form.html'
    form_class = ProductModelForm
    success_url = "/products/"
    submit_btn = 'Update Product'


class ProductDetailView(MultipleSlugMixin, DetailView):
    model = Product


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        qs = super(ProductListView, self).get_queryset()
        # qs = qs.filter(title__icontains="test")
        return qs


def create_view(request):
    # FORM
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        print form.data
        print form.data.get("publish")
        print form.cleaned_data
        print form.cleaned_data.get("publish")
        instance = form.save(commit=False)
        instance.sale_price = instance.price
        instance.save()

    template = "form.html"
    context = {
        "form": form,
        "submit_btn": "Create Product"
    }
    return render(request, template, context)


def update_view(request, object_id=None):
    product = get_object_or_404(Product, id=object_id)
    form = ProductModelForm(request.POST or None, instance=product)
    if form.is_valid():
        print form.data
        print form.data.get("publish")
        print form.cleaned_data
        print form.cleaned_data.get("publish")
        instance = form.save(commit=False)
        instance.sale_price = instance.price
        instance.save()
    template = "form.html"
    context = {
        "object": product,
        "form": form,
        "submit_btn": "Update Product"
    }
    return render(request, template, context)


def detail_slug_view(request, slug=None):
    product = Product.objects.get(slug=slug)
    try:
        product = get_object_or_404(Product, slug=slug)
    except Product.MultipleObjectsReturned:
        product = Product.objects.filter(slug=slug).order_by("-title").first()
    # print slug
    # product = 1
    template = "detail_view.html"
    context = {
        "object": product
    }
    return render(request, template, context)


def detail_view(request, object_id=None):
    product = get_object_or_404(Product, id=object_id)
    template = "detail_view.html"
    context = {
        "object": product
    }
    return render(request, template, context)


# if object_id is not None:
# 	product = get_object_or_404(Product, id=object_id)
# 	# product = Product.objects.get(id=object_id)
# 	# try:
# 	# 	product = Product.objects.get(id=object_id)
# 	# except Product.DoesNotExist:
# 	# 	product = None


# else:
# 	raise Http404


def list_view(request):
    # list of items
    print request
    queryset = Product.objects.all()
    template = "list_view.html"
    context = {
        "queryset": queryset
    }
