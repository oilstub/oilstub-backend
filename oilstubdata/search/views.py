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

from oilandgasdata.documents import (
    GpCountyDocument,
    OgWellCompletionDocument,
    OgSummaryOnShoreLeaseDocument,
    OgSummaryMasterLarge,
    OgRegulatoryLeaseDwDocument,
)
from search.serializers import (
    GpCountyDocumentSerializer,
    OgWellCompletionDocumentSerializer,
    OgSummaryOnShoreLeaseDocumentSerializer,
    OgSummaryMasterLargeSerializer,
    OgRegulatoryLeaseDwDocumentSerializer,
)


class BaseDocumentView(DocumentViewSet):
    document = None
    serializer_class = None
    ordering = ('created_at',)

    filter_backends = [
        DefaultOrderingFilterBackend,
        CompoundSearchFilterBackend,
        FilteringFilterBackend,
        SuggesterFilterBackend,
    ]


class GpCountySearchView(BaseDocumentView):
    document = GpCountyDocument
    serializer_class = GpCountyDocumentSerializer

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
        'district_name': {
            'field': 'district_name.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },
        'district_no': {
            'field': 'district_no.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

        'county_no': {
            'field': 'county_no.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

        'county_name': {
            'field': 'county_name.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

    }


class OgWellCompletionDocumentViewSet(BaseDocumentView):
    document = OgWellCompletionDocument
    serializer_class = OgWellCompletionDocumentSerializer

    search_fields = (
        'district_name',
        'district_no',
        'county_name',
        'county_no',
        'lease_no',
        'well_no',
    )

    filter_fields = {
        'district_name': 'district_name',
        'district_no': 'district_no',
        'county_name': 'county_name',
        'county_no': 'county_no',
        'lease_no': 'lease_no',
        'well_no': 'well_no'
    }

    suggester_fields = {
        'district_name': {
            'field': 'district_name.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },
        'district_no': {
            'field': 'district_no.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

        'county_no': {
            'field': 'county_no.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

        'county_name': {
            'field': 'county_name.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

        'lease_no': {
            'field': 'lease_no.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

        'well_no': {
            'field': 'well_no.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

    }


class OgSummaryOnShoreLeaseDocumentViewSet(BaseDocumentView):
    document = OgSummaryOnShoreLeaseDocument
    serializer_class = OgSummaryOnShoreLeaseDocumentSerializer

    search_fields = (
        'district_name',
        'district_no',
        'lease_name',
        'lease_no',
        'field_nname',
        'field_no',
        'operation_name',
        'operation_no'
    )

    filter_fields = {
        'district_name': 'district_name',
        'district_no': 'district_no',
        'lease_name': 'lease_name',
        'lease_no': 'lease_no',
        'field_no': 'field_no',
        'field_name': 'field_name',
        'operation_name': 'operation_name',
        'operation_no': 'operation_no'
    }

    suggester_fields = {
        'district_name': {
            'field': 'district_name.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },
        'district_no': {
            'field': 'district_no.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

        'lease_no': {
            'field': 'lease_no.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

        'lease_name': {
            'field': 'lease_name.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

        'field_no': {
            'field': 'field_no.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

        'field_name': {
            'field': 'field_nam.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },
        'operator_no': {
            'field': 'operator_no.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

        'operator_name': {
            'field': 'operator_name.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

    }


class OgSummaryMasterLargeViewSet(BaseDocumentView):
    document = OgSummaryMasterLarge
    serializer_class = OgSummaryMasterLargeSerializer

    search_fields = (
        'district_name',
        'district_no',
        'lease_no',
        'field_nname',
        'field_no',
        'operation_name',
        'operation_no'
    )

    filter_fields = {
        'district_name': 'district_name',
        'district_no': 'district_no',
        'lease_no': 'lease_no',
        'field_no': 'field_no',
        'field_name': 'field_name',
        'operation_name': 'operation_name',
        'operation_no': 'operation_no'
    }

    suggester_fields = {
        'district_name': {
            'field': 'district_name.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },
        'district_no': {
            'field': 'district_no.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

        'lease_no': {
            'field': 'lease_no.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

        'field_no': {
            'field': 'field_no.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

        'field_name': {
            'field': 'field_nam.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },
        'operator_no': {
            'field': 'operator_no.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

        'operator_name': {
            'field': 'operator_name.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

    }


class OgRegulatoryLeaseDwDocumentViewSet(BaseDocumentView):
    document = OgRegulatoryLeaseDwDocument
    serializer_class = OgRegulatoryLeaseDwDocumentSerializer

    search_fields = (
        'district_name',
        'district_no',
        'lease_name',
        'lease_no',
        'field_nname',
        'field_no',
        'operation_name',
        'operation_no',
        'well_no'
    )

    filter_fields = {
        'district_name': 'district_name',
        'district_no': 'district_no',
        'lease_name': 'lease_name',
        'lease_no': 'lease_no',
        'field_no': 'field_no',
        'field_name': 'field_name',
        'operation_name': 'operation_name',
        'operation_no': 'operation_no',
        'well_no': 'well_no'
    }

    suggester_fields = {
        'district_name': {
            'field': 'district_name.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },
        'district_no': {
            'field': 'district_no.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

        'lease_no': {
            'field': 'lease_no.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

        'lease_name': {
            'field': 'lease_name.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

        'field_no': {
            'field': 'field_no.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

        'field_name': {
            'field': 'field_nam.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },
        'operator_no': {
            'field': 'operator_no.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

        'operator_name': {
            'field': 'operator_name.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },
        'well_no': {
            'field': 'well_no.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },

    }
