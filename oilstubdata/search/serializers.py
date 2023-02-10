from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from oilandgasdata.documents import (
    GpCountyDocument,
    OgWellCompletionDocument,
    OgSummaryOnShoreLeaseDocument,
    OgSummaryMasterLarge,
    OgRegulatoryLeaseDwDocument,
    OgOperatorDwDocument,
    OgOperatorCycleDocument,
    OgLeaseCycleDispDocument,
    OgLeaseCycleDocument,
    OgFieldDwDocument,
    OgDistrictCycleDocument,
    OgFieldCycleDocument,
    OgCountyCycleDocument,
    GpDistrictDocument,
    GpDateRangeCycleDocument,
    OgCountyLeaseCycleDocument
)


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


class OgWellCompletionDocumentSerializer(DocumentSerializer):

    class Meta:
        document = OgWellCompletionDocument
        fields = (
            'district_name',
            'district_no',
            'county_name',
            'county_no',
            'lease_no',
            'well_no',
            'created_at',
            'oil_gas_code',
            "api_county_code",
            "api_unique_no",
            "onshore_assc_cnty",
            "oil_well_unit_no",
            "well_root_no",
            "wellbore_shutin_dt",
            "well_shutin_dt",
            "well_14b2_status_code",
            "well_subject_14b2_flag",
            "wellbore_location_code",

        )


class OgSummaryOnShoreLeaseDocumentSerializer(DocumentSerializer):

    class Meta:
        document = OgSummaryOnShoreLeaseDocument
        fields = (
            'district_name',
            'district_no',
            'lease_name',
            'lease_no',
            'field_no',
            'field_name',
            'operator_no',
            'operator_name',
            'created_at',
            'oil_gas_code',
            "cycle_year_month_min",
            "cycle_year_month_max",
        )


class OgSummaryMasterLargeSerializer(DocumentSerializer):

    class Meta:
        document = OgSummaryMasterLarge
        fields = (
            'district_name',
            'district_no',
            'lease_no',
            'field_no',
            'field_name',
            'operator_no',
            'operator_name',
            'created_at',
            'oil_gas_code',
            'cycle_year_month_min',
            'cycle_year_month_max',
        )


class OgRegulatoryLeaseDwDocumentSerializer(DocumentSerializer):

    class Meta:
        document = OgRegulatoryLeaseDwDocument
        fields = (
            'district_name',
            'district_no',
            'lease_name',
            'lease_no',
            'field_no',
            'field_name',
            'operator_no',
            'operator_name',
            'well_no',
            'created_at',
            'oil_gas_code',
            'lease_off_sched_flag',
            'lease_severance_flag',
        )


class OgOperatorDwDocumentSerializer(DocumentSerializer):

    class Meta:
        document = OgOperatorDwDocument
        fields = (
            'operator_no',
            'operator_name',
            'created_at',
            'p5_status_code',
            'p5_last_filed_dt',
            'operator_tax_cert_flag',
            'operator_sb639_flag',
            'fa_option_code',
            'record_status_code',
            'efile_status_code',
            'efile_effective_dt',
            'create_by',
            'create_dt',
            'modify_by',
            'modify_dt',
        )


class OgOperatorCycleDocumentSerializer(DocumentSerializer):

    class Meta:
        document = OgOperatorCycleDocument
        fields = (
            'operator_no',
            'operator_name',
            'created_at',
            'cycle_year',
            'cycle_month',
            'cycle_year_month',
            'oper_oil_prod_vol',
            'oper_gas_prod_vol',
            'oper_cond_prod_vol',
            'oper_csgd_prod_vol',
        )


class OgLeaseCycleDispDocumentSerializer(DocumentSerializer):

    class Meta:
        document = OgLeaseCycleDispDocument
        fields = (
            'district_name',
            'district_no',
            'lease_name',
            'lease_no',
            'field_no',
            'field_name',
            'operator_no',
            'operator_name',
            'created_at',
            'oil_gas_code',
            'cycle_year',
            'cycle_month',
            'cycle_year_month',
            'lease_oil_dispcd00_vol',
            'lease_oil_dispcd01_vol',
            'lease_oil_dispcd02_vol',
            'lease_oil_dispcd03_vol',
            'lease_oil_dispcd04_vol',
            'lease_oil_dispcd05_vol',
            'lease_oil_dispcd06_vol',
            'lease_oil_dispcd07_vol',
            'lease_oil_dispcd09_vol',
            'lease_oil_dispcd99_vol',
            'lease_gas_dispcd01_vol',
            'lease_gas_dispcd02_vol',
            'lease_gas_dispcd03_vol',
            'lease_gas_dispcd04_vol',
            'lease_gas_dispcd05_vol',
            'lease_gas_dispcd06_vol',
            'lease_gas_dispcd07_vol',
            'lease_gas_dispcd08_vol',
            'lease_gas_dispcd09_vol',
            'lease_gas_dispcd99_vol',
            'lease_cond_dispcd00_vol',
            'lease_cond_dispcd01_vol',
            'lease_cond_dispcd02_vol',
            'lease_cond_dispcd03_vol',
            'lease_cond_dispcd04_vol',
            'lease_cond_dispcd05_vol',
            'lease_cond_dispcd06_vol',
            'lease_cond_dispcd07_vol',
            'lease_cond_dispcd08_vol',
            'lease_cond_dispcd09_vol',
            'lease_cond_dispcd99_vol',
            'lease_csgd_dispcd01_vol',
            'lease_csgd_dispcd02_vol',
            'lease_csgd_dispcd03_vol',
            'lease_csgd_dispcd04_vol',
            'lease_csgd_dispcd05_vol',
            'lease_csgd_dispcd06_vol',
            'lease_csgd_dispcd07_vol',
            'lease_csgd_dispcd08_vol',
            'lease_csgd_dispcd09_vol',
            'lease_csgd_dispcd99_vol',
        )


class OgLeaseCycleDocumentSerializer(DocumentSerializer):

    class Meta:
        document = OgLeaseCycleDocument
        fields = (
            'district_name',
            'district_no',
            'lease_name',
            'lease_no',
            'field_no',
            'field_name',
            'operator_no',
            'operator_name',
            'created_at',
            'oil_gas_code',
            'cycle_year_month_min',
            'cycle_year_month_max',
        )


class OgFieldDwDocumentSerializer(DocumentSerializer):

    class Meta:
        document = OgFieldDwDocument
        fields = (
            'district_name',
            'district_no',
            'field_no',
            'field_name',
            'created_at',
            'field_class',
            'field_h2s_flag',
            'field_manual_rev_flag',
            'wildcat_flag',
            'o_derived_rule_type_code',
            'g_derived_rule_type_code',
            'o_rescind_dt',
            'g_rescind_dt',
            'o_salt_dome_flag',
            'g_salt_dome_flag',
            'o_offshore_code',
            'g_offshore_code',
            'o_dont_permit',
            'g_dont_permit',
            'o_noa_man_rev_rule',
            'g_noa_man_rev_rule',
            'o_county_no',
            'g_county_no',
            'o_discovery_dt',
            'g_discovery_dt',
            'o_sched_remarks',
            'g_sched_remarks',
            'o_comments',
            'g_comments',
            'create_by',
            'create_dt',
            'modify_by',
            'modify_dt',
        )


class OgDistrictCycleDocumentSerializer(DocumentSerializer):

    class Meta:
        document = OgDistrictCycleDocument
        fields = (
            'district_name',
            'district_no',
            'created_at',
            'cycle_year',
            'cycle_month',
            'cycle_year_month',
            'dist_oil_prod_vol',
            'dist_gas_prod_vol',
            'dist_cond_prod_vol',
            'dist_csgd_prod_vol',
        )


class OgFieldCycleDocumentSerializer(DocumentSerializer):

    class Meta:
        document = OgFieldCycleDocument
        fields = (
            'district_name',
            'district_no',
            'field_no',
            'field_name',
            'created_at',
            'cycle_year',
            'cycle_month',
            'cycle_year_month',
            'field_oil_prod_vol',
            'field_gas_prod_vol',
            'field_cond_prod_vol',
            'field_csgd_prod_vol',
        )


class OgCountyCycleDocumentSerializer(DocumentSerializer):

    class Meta:
        document = OgCountyCycleDocument
        fields = (
            'district_name',
            'district_no',
            'county_no',
            'county_name',
            'created_at',
            'cycle_year',
            'cycle_month',
            'cycle_year_month',
            'cnty_oil_prod_vol',
            'cnty_oil_allow',
            'cnty_oil_ending_bal',
            'cnty_gas_prod_vol',
            'cnty_gas_allow',
            'cnty_gas_lift_inj_vol',
            'cnty_cond_prod_vol',
            'cnty_cond_limit',
            'cnty_cond_ending_bal',
            'cnty_csgd_prod_vol',
            'cnty_csgd_limit',
            'cnty_csgd_gas_lift',
            'cnty_oil_tot_disp',
            'cnty_gas_tot_disp',
            'cnty_cond_tot_disp',
            'cnty_csgd_tot_disp',
            'oil_gas_code',
        )


class GpDistrictDocumentSerializer(DocumentSerializer):

    class Meta:
        document = GpDistrictDocument
        fields = (
            'district_name',
            'district_no',
            'created_at',
            'office_phone_no',
            'office_location',
        )


class GpDateRangeCycleDocumentSerializer(DocumentSerializer):

    class Meta:
        document = GpDateRangeCycleDocument
        fields = (
            'created_at',
            'oldest_prod_cycle_year_month',
            'newest_prod_cycle_year_month',
            'newest_sched_cycle_year_month',
            'gas_extract_date',
            'oil_extract_date',
        )


class OgCountyLeaseCycleDocumentSerializer(DocumentSerializer):

    class Meta:
        document = OgCountyLeaseCycleDocument
        fields = (
            'district_name',
            'district_no',
            'lease_name',
            'lease_no',
            'field_name',
            'field_no',
            'county_name',
            'county_no',
            'operator_name',
            'operator_no',
            'created_at',
            'oil_gas_code',
            'cycle_year',
            'cycle_month',
            'cycle_year_month',
            'field_type',
            'gas_well_no',
            'prod_report_field_flag',
            'cnty_lse_oil_prod_vol',
            'cnty_lse_oil_allow',
            'cnty_lse_oil_ending_bal',
            'cnty_lse_gas_prod_vol',
            'cnty_lse_gas_allow',
            'cnty_lse_gas_lift_inj_vol',
            'cnty_lse_cond_prod_vol',
            'cnty_lse_cond_limit',
            'cnty_lse_cond_ending_bal',
            'cnty_lse_csgd_prod_vol',
            'cnty_lse_csgd_limit',
            'cnty_lse_csgd_gas_lift',
            'cnty_lse_oil_tot_disp',
            'cnty_lse_gas_tot_disp',
            'cnty_lse_cond_tot_disp',
            'cnty_lse_csgd_tot_disp',
        )

