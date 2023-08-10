from django import forms

from jeonse.models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            "creator",
            "jeonse_deposit_amount",
            "wolse_deposit_amount",
            "wolse_monthly_payment",
            "gwanlibi_monthly_payment",
            "annual_interest_rate",
            "total_area",
            "number_of_rooms",
            "number_of_bathrooms",
            "comment",
        ]
