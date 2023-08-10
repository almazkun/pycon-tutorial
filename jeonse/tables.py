import django_tables2 as tables

from jeonse.models import Listing


class ListingTable(tables.Table):
    get_absolute_url = tables.Column(
        verbose_name="Detail", linkify=True, orderable=False
    )

    class Meta:
        model = Listing
        template_name = "django_tables2/bootstrap5.html"
        attrs = {"class": "table table-striped table-bordered table-hover"}

    def render_get_absolute_url(self, value):
        return "Detail"
