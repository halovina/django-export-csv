import csv
from django.http import HttpResponse
from product.models import Product
import datetime


def export_to_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="export_csv_{}.csv"'.format(datetime.datetime.now())},
    )

    writer = csv.writer(response)
    writer.writerow(["Product Name", "Base Price", "Selling Price", "CreatedAt","UpdatedAt"])
    
    all_product = Product.objects.all()
    for x in all_product:
        writer.writerow([x.product_name, x.hpp, x.selling_price, x.created_date, x.update_date])

    return response