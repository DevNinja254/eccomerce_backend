from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import pagination
class CustomPagination(PageNumberPagination):
    page_size_query_param = "page_size"
    page_query_param = "page"
    max_page_size = 20
    def get_paginated_response(self, data):
        return Response({
            'next':self.get_next_link(),
            'previous': self.get_previous_link(),
            'count':self.page.paginator.count,
            'page_size': self.page_size,
            'results':data,
        })
        
class OptionalPagination(pagination.PageNumberPagination):
    def paginate_queryset(self, queryset, request, view=None):
        if request.query_params.get('paginate') == 'false':
            return None  # Disable pagination
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        if data is None:
            return Response(self.serializer_class(self.queryset, many=True).data)
        return super().get_paginated_response(data)