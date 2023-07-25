from typing import List
from django_tables2 import SingleTableView
from django_filters.views import FilterView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from jeonse.filters import ListingFilter
from jeonse.forms import ListingForm
from jeonse.mixins import UserIsCreatorMixin
from jeonse.models import Listing
from jeonse.tables import ListingTable


class ListingListView(LoginRequiredMixin, FilterView, SingleTableView):
    model = Listing
    template_name = "listing_list.html"
    table_class = ListingTable
    filterset_class = ListingFilter

    def get_queryset(self):
        return Listing.objects.filter(creator=self.request.user)

    def get_template_names(self) -> List[str]:
        if self.request.htmx:
            return ["htmx/listing_list.html"]
        return super().get_template_names()


class ListingDetailView(LoginRequiredMixin, UserIsCreatorMixin, DetailView):
    model = Listing
    template_name = "listing_detail.html"


class ListingCreateView(LoginRequiredMixin, CreateView):
    model = Listing
    form_class = ListingForm
    template_name = "listing_create.html"
    success_url = reverse_lazy("listing_list")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
