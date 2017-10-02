from django.shortcuts import render
from .models import Product
# login required experiment
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class ProductView(LoggedInMixin):
        model = Product
        template_name = 'blogposts.html'

        def get_queryset(self):
            return Product.objects.filter(owner=self.request.user)
# login required experiment


def all_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products})