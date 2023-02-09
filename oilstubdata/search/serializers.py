from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from oilandgasdata.documents import GpCountyDocument


class GpCountyDocumentSerializer(DocumentSerializer):
    class Meta:
        document = GpCountyDocument
        fields = (
            'district_name',
            'district_no',
            'county_name',
            'county_no',
            'created_at',
            'county_fips_code',
            'on_shore_flag',
            'onshore_assc_cnty_flag',
        )

