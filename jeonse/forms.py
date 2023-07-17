from django import forms
from jeonse.models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = "__all__"
