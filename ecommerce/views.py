from django.shortcuts import render
from store.models import Product, ReviewRating
from django.views import View

class DashboardView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all().filter(is_available=True).order_by('created_date')

        for product in products:
            reviews = ReviewRating.objects.filter(product_id=product.id, status=True)


        context = {
            'products': products,
        }

        return render(request, 'home.html', context)
