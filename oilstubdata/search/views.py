import abc

from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView

from oilandgasdata.documents import OgDistrictCycleDocument, GpCountyDocument
from oilandgasdata.serializers import GpCountySerializer
from search.core.business_logics.elastic_search import ElasticSearchQuery
from search.serializers import SearchSerializer


class PaginatedElasticSearchAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def get_q_expression(self, query):
        """This method should be overridden
        and return a Q() expression."""

    def get(self, request, query):
        try:
            q = self.get_q_expression(query)
            search = self.document_class.search().query(q)
            response = search.execute()

            print(f'Found {response.hits.total.value} hit(s) for query: "{query}"')

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)

#
# class DistrictCycleSearchView(PaginatedElasticSearchAPIView):
#     document_class = OgDistrictCycleDocument
#
#     def get_q_expression(self, query):
#         return


class GpCountySearchView(PaginatedElasticSearchAPIView):
    serializer_class = GpCountySerializer
    document_class = GpCountyDocument

    def get_q_expression(self, query):
        search_query = ElasticSearchQuery(query).generate_q_expression()
        return search_query


# class SearchViewSet(APIView):
#     permission_classes = []
#
#     def post(self, request, *args, **kwargs):
#         serializer = SearchSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             response = serializer.save()
#             return Response(response, status=status.HTTP_200_OK)
#         return Response({"message": 'Invalid search term'}, status=status.HTTP_400_BAD_REQUEST)





