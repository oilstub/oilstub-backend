import abc

from django.http import HttpResponse
from elasticsearch_dsl import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView

from oilandgasdata.documents import OgDistrictCycleDocument


class PaginatedElasticSearchAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """This method should be overridden
        and return a Q() expression."""

    def get(self, request, query):
        try:
            q = self.generate_q_expression(query)
            search = self.document_class.search().query(q)
            response = search.execute()

            print(f'Found {response.hits.total.value} hit(s) for query: "{query}"')

            results = self.paginate_queryset(response, request, view=self)
            # serializer = self.serializer_class(results, many=True)
            return self.get_paginated_response(results)
        except Exception as e:
            return HttpResponse(e, status=500)


class DistrictCycleSearchView(PaginatedElasticSearchAPIView):
    document_class = OgDistrictCycleDocument

    def generate_q_expression(self, query):
        return Q('bool',
                 should=[
                     Q('match', district_name=query),
                     Q('match', district_n0=query),
                 ], minimum_should_match=1)




