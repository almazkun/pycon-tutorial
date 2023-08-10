from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from jeonse.forms import ListingForm
from jeonse.models import Listing


class ListingListView(ListView):
    model = Listing
    template_name = "jeonse/listing_list.html"


class ListingDetailView(DetailView):
    model = Listing
    template_name = "jeonse/listing_detail.html"


class ListingCreateView(CreateView):
    model = Listing
    form_class = ListingForm
    template_name = "jeonse/listing_create.html"
    success_url = reverse_lazy("listing_list")
