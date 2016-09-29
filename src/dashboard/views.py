import random

from django.shortcuts import render
from django.views.generic import View

from products.models import Product


# Create your views here.

class DashboardView(View):
    def get(self, request, *args, **kwargs):
        print request
        print request.user
        tag_views = None
        products = None
        top_tags = None
        try:
            tag_views = request.user.tagview_set.all().order_by("-count")[:5]
        except:
            pass

        owned = None

        try:
            owned = request.user.myproducts.products.all()
        except:
            pass

        if tag_views:
            top_tags = [x.tag for x in tag_views]
            products = Product.objects.filter(tag__in=top_tags)
            if owned:
                products = products.exclude(pk__in=owned)
            products = products.distinct()
            print products
            print top_tags
            products = sorted(products, key=lambda x: random.random())

        context = {
            "products": products,
            "top_tags": top_tags,
        }

        return render(request, "dashboard/view.html", context)
