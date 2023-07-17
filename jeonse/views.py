from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from jeonse.forms import ListingForm
from jeonse.models import Listing


class ListingListView(ListView):
    model = Listing
    template_name = "listing_list.html"


class ListingDetailView(DetailView):
    model = Listing
    template_name = "listing_detail.html"


class ListingCreateView(CreateView):
    model = Listing
    form_class = ListingForm
    template_name = "listing_create.html"
    success_url = reverse_lazy("listing_list")
