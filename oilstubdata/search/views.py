from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    SUGGESTER_COMPLETION,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    SearchFilterBackend,
    DefaultOrderingFilterBackend,
    FilteringFilterBackend,
    CompoundSearchFilterBackend,
    SuggesterFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from oilandgasdata.documents import GpCountyDocument
from search.serializers import GpCountyDocumentSerializer


class BaseDocumentView(DocumentViewSet):
    document = None
    serializer_class = None

    filter_backends = [DefaultOrderingFilterBackend]


class GpCountySearchView(BaseDocumentView):
    document = GpCountyDocument
    serializer_class = GpCountyDocumentSerializer
    ordering = ('created_at',)

    filter_backends = [
        CompoundSearchFilterBackend
    ]

    search_fields = (
        'district_name',
        'district_no',
        'county_name',
        'county_no'
    )


class GpCountyFilterView(BaseDocumentView):
    document = GpCountyDocument
    serializer_class = GpCountyDocumentSerializer
    ordering = ('created_at',)

    filter_backends = [
        FilteringFilterBackend
    ]

    filter_fields = {
        'district_name': 'district_name',
        'district_no': 'district_no',
        'county_name': 'county_name',
        'county_no': 'county_no'
    }


class GpCountyCompletionView(BaseDocumentView):
    document = GpCountyDocument
    serializer_class = GpCountyDocumentSerializer
    ordering = ('created_at',)

    filter_backends = [
        SuggesterFilterBackend
    ]

    suggester_fields = {
        'district_name': {
            'field': 'district_name.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },
    }
