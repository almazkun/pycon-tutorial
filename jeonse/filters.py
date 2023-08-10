import django_filters
from django import forms

from jeonse.models import Listing


class ListingFilter(django_filters.FilterSet):
    total_monthly_payment = django_filters.NumberFilter(
        field_name="total_monthly_payment",
        lookup_expr="lte",
        widget=forms.widgets.TextInput(attrs={"class": "form-control form-control-sm"}),
    )

    class Meta:
        model = Listing
        fields = ["total_monthly_payment"]
