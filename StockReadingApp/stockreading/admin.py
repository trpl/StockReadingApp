from django.contrib import admin

from .models import StockReading

class StockReadingAdmin(admin.ModelAdmin):
    get_latest_by = 'created_on'
    ordering = ('-created_on', )
    search_fields = ('id', 'reference_id')
    list_display = ('id', 'reference_id', 'expiry_date', 'created_on')
    list_filter = ('expiry_date', 'created_on')

admin.site.register(StockReading, StockReadingAdmin)
