from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import StockReading

class StockReadingCreateView(CreateView):
    model = StockReading
    fields = ['reference_id', 'expiry_date']
    template_name = 'create_reading.html'

    def get_context_data(self, **kwargs):
        context = super(StockReadingCreateView, self).get_context_data(**kwargs)
        context['success'] = self.request.GET.get('success')
        return context

class StockReadingListingView(ListView):
    model = StockReading
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super(StockReadingListingView, self).get_context_data(**kwargs)
        context['reference_id'] = self.request.GET.get('reference_id')
        return context


class CurrentListingView(StockReadingListingView):
    template_name = 'current_listing.html'
    
    def get_queryset(self):
        kwargs = dict()
        reference_id = self.request.GET.get('reference_id')
        if reference_id:
            kwargs["reference_id"] = reference_id
        return StockReading.objects.filter_current(**kwargs).order_by(
            'expiry_date', 'reference_id'
        )


class HistoricListingView(StockReadingListingView):
    template_name = 'historic_listing.html'

    def get_queryset(self):
        kwargs = dict()
        reference_id = self.request.GET.get('reference_id')
        if reference_id:
            kwargs["reference_id"] = reference_id
        return StockReading.objects.filter_historic(**kwargs).order_by(
            'expiry_date', 'reference_id'
        )