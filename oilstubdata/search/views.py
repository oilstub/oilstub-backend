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
    DefaultOrderingFilterBackend,
    FilteringFilterBackend,
    CompoundSearchFilterBackend,
    SuggesterFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from oilandgasdata.documents import GpCountyDocument
from search.serializers import GpCountyDocumentSerializer


class GpCountySearchView(DocumentViewSet):
    document = GpCountyDocument
    serializer_class = GpCountyDocumentSerializer
    ordering = ('created_at',)

    filter_backends = [
        DefaultOrderingFilterBackend,
        FilteringFilterBackend,
        CompoundSearchFilterBackend,
        SuggesterFilterBackend,
    ]

    search_fields = (
        'district_name',
        'district_no',
        'county_name',
        'county_no'
    )

    filter_fields = {
        'district_name': 'district_name',
        'district_no': 'district_no',
        'county_name': 'county_name',
        'county_no': 'county_no'
    }

    suggester_fields = {
        'district_name_suggest': {
            'field': 'district_name.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
            'options': {
                'size': 20,  # Override default number of suggestions
                'skip_duplicates': True,  # Whether duplicate suggestions should be filtered out.
            },
        },
    }


