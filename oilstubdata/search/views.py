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
from rest_framework import permissions

from oilandgasdata.documents import (
    GpCountyDocument,
    OgWellCompletionDocument,
    OgSummaryOnShoreLeaseDocument,
    OgSummaryMasterLarge,
    OgRegulatoryLeaseDwDocument,
    OgOperatorDwDocument,
    OgOperatorCycleDocument,
    OgLeaseCycleDispDocument,
    OgFieldDwDocument,
    OgDistrictCycleDocument,
    OgFieldCycleDocument,
    OgCountyCycleDocument,
    GpDistrictDocument,
    GpDateRangeCycleDocument,
    OgCountyLeaseCycleDocument,
    OgLeaseCycleDocument,
)
from search.serializers import (
    GpCountyDocumentSerializer,
    OgWellCompletionDocumentSerializer,
    OgSummaryOnShoreLeaseDocumentSerializer,
    OgSummaryMasterLargeSerializer,
    OgRegulatoryLeaseDwDocumentSerializer,
    OgOperatorDwDocumentSerializer,
    OgOperatorCycleDocumentSerializer,
    OgLeaseCycleDispDocumentSerializer,
    OgFieldDwDocumentSerializer,
    OgDistrictCycleDocumentSerializer,
    OgFieldCycleDocumentSerializer,
    OgCountyCycleDocumentSerializer,
    GpDistrictDocumentSerializer,
    GpDateRangeCycleDocumentSerializer,
    OgCountyLeaseCycleDocumentSerializer,
    OgLeaseCycleDocumentSerializer,
)


class BaseDocumentView(DocumentViewSet):
    document = None
    serializer_class = None
    permission_classes = [permissions.IsAuthenticated]
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
        'field_name',
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
        'field_name',
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
        'field_name',
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


class OgOperatorDwDocumentViewSet(BaseDocumentView):
    document = OgOperatorDwDocument
    serializer_class = OgOperatorDwDocumentSerializer

    search_fields = (
        'operation_name',
        'operation_no'
    )

    filter_fields = {
        'operation_name': 'operation_name',
        'operation_no': 'operation_no',
    }

    suggester_fields = {
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
        }

    }


class OgOperatorCycleDocumentViewSet(OgOperatorDwDocumentViewSet):
    document = OgOperatorCycleDocument
    serializer_class = OgOperatorCycleDocumentSerializer


class OgLeaseCycleDispDocumentViewSet(BaseDocumentView):
    document = OgLeaseCycleDispDocument
    serializer_class = OgLeaseCycleDispDocumentSerializer

    search_fields = (
        'district_name',
        'district_no',
        'lease_name',
        'lease_no',
        'field_name',
        'field_no',
        'operation_name',
        'operation_no',
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
        }

    }


class OgFieldDwDocumentViewSet(BaseDocumentView):
    document = OgFieldDwDocument
    serializer_class = OgFieldDwDocumentSerializer

    search_fields = (
        'district_name',
        'district_no',
        'field_name',
        'field_no',
    )

    filter_fields = {
        'district_name': 'district_name',
        'district_no': 'district_no',
        'field_no': 'field_no',
        'field_name': 'field_name'
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
        }

    }


class OgDistrictCycleDocumentViewSet(BaseDocumentView):
    document = OgDistrictCycleDocument
    serializer_class = OgDistrictCycleDocumentSerializer

    search_fields = (
        'district_name',
        'district_no'
    )

    filter_fields = {
        'district_name': 'district_name',
        'district_no': 'district_no'
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
        }

    }


class OgFieldCycleDocumentViewSet(OgFieldDwDocumentViewSet):
    document = OgFieldCycleDocument
    serializer_class = OgFieldCycleDocumentSerializer


class OgCountyCycleDocumentViewSet(GpCountySearchView):
    document = OgCountyCycleDocument
    serializer_class = OgCountyCycleDocumentSerializer


class GpDistrictDocumentViewSet(OgDistrictCycleDocumentViewSet):
    document = GpDistrictDocument
    serializer_class = GpDistrictDocumentSerializer


class GpDateRangeCycleDocumentViewSet(BaseDocumentView):
    document = GpDateRangeCycleDocument
    serializer_class = GpDateRangeCycleDocumentSerializer

    search_fields = (
        'gas_extract_date',
        'gas_extract_date'
    )

    filter_fields = {
        'oil_extract_date': 'oil_extract_date',
        'gas_extract_date': 'gas_extract_date'
    }

    suggester_fields = {
        'oil_extract_date': {
            'field': 'oil_extract_date.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        },
        'gas_extract_date': {
            'field': 'gas_extract_date.suggest',
            'default_suggester': [
                SUGGESTER_COMPLETION,
            ],
        }

    }


class OgCountyLeaseCycleDocumentViewSet(BaseDocumentView):
    document = OgCountyLeaseCycleDocument
    serializer_class = OgCountyLeaseCycleDocumentSerializer

    search_fields = (
        'district_name',
        'district_no',
        'lease_name',
        'lease_no',
        'county_no',
        'county_name',
        'field_name',
        'field_no',
        'operation_name',
        'operation_no',
    )

    filter_fields = {
        'district_name': 'district_name',
        'district_no': 'district_no',
        'county_no': 'county_no',
        'county_name': 'county_name',
        'lease_name': 'lease_name',
        'lease_no': 'lease_no',
        'field_no': 'field_no',
        'field_name': 'field_name',
        'operation_name': 'operation_name',
        'operation_no': 'operation_no',
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
        }

    }


class OgLeaseCycleDocumentViewSet(OgLeaseCycleDispDocumentViewSet):
    document = OgLeaseCycleDocument
    serializer_class = OgLeaseCycleDocumentSerializer
