from django_filters import rest_framework as filters
from django_filters.rest_framework import DateFromToRangeFilter
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = DateFromToRangeFilter(field_name='created_at', lookup_expr='lt')
    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator','status',]
