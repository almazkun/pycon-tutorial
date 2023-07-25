import django_filters

from jeonse.models import Listing


class ListingFilter(django_filters.FilterSet):
    class Meta:
        model = Listing
        fields = {
            "jeonse_deposit_amount": ["lte",],
            "wolse_deposit_amount": ["lte",],
            "total_monthly_payment": ["lte",],
        }