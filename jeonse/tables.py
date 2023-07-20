import django_tables2 as tables

from jeonse.models import Listing

class ListingTable(tables.Table):
    class Meta:
        model = Listing
        template_name = "django_tables2/bootstrap5.html"
