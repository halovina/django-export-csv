from django.shortcuts import render
from django.views.generic.base import TemplateView
from product import models

# Create your views here.

class ProductView(TemplateView):
    template_name = "product/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_product"] = models.Product.objects.all()
        return context
