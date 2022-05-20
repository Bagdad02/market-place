from django_filters import rest_framework as filters

from post.models import Post


class PostFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    price_from = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_to = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Post
        fields = ['name', 'price_from', 'price_to', 'category', 'status']

