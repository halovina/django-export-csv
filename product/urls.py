from django.urls import path
from . import views
from . import export_csv

urlpatterns = [
    path('list/', views.ProductView.as_view(), name='product_list'),
    path('exportcsv', export_csv.export_to_csv, name='product_export_csv')
]