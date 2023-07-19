from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from jeonse.forms import ListingForm
from jeonse.models import Listing
from django.contrib.auth.mixins import LoginRequiredMixin
from jeonse.mixins import UserIsCreatorMixin


class ListingListView(LoginRequiredMixin, ListView):
    model = Listing
    template_name = "listing_list.html"

    def get_queryset(self):
        return Listing.objects.filter(creator=self.request.user)


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
