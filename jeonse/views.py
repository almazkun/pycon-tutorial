from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django_tables2 import SingleTableView

from jeonse.forms import ListingForm
from jeonse.mixins import UserIsAuthenticatedMixin, UserIsCreatorMixin
from jeonse.models import Listing
from jeonse.tables import ListingTable


class ListingListView(UserIsAuthenticatedMixin, SingleTableView):
    model = Listing
    template_name = "jeonse/listing_list.html"
    table_class = ListingTable

    def get_queryset(self):
        return self.request.user.listings.all()


class ListingDetailView(UserIsAuthenticatedMixin, UserIsCreatorMixin, DetailView):
    model = Listing
    template_name = "jeonse/listing_detail.html"


class ListingCreateView(UserIsAuthenticatedMixin, CreateView):
    model = Listing
    form_class = ListingForm
    template_name = "jeonse/listing_create.html"
    success_url = reverse_lazy("listing_list")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
