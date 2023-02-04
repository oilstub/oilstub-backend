from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from oilandgasdata.models import (
    OgWellCompletion,
    OgSummaryOnShoreLease,
    OgSummaryMasterLarge,
    GpCounty,
    OgLeaseCycleDisp,
    GpDistrict,
    GpDateRangeCycle,
    OgCountyCycle,
    OgCountyLeaseCycle,
    OgDistrictCycle,
    OgFieldCycle,
    OgFieldDw,
    OgOperatorCycle,
    OgOperatorDw,
    OgRegulatoryLeaseDw,
    OgLeaseCycle,
)


@registry.register_document
class OgWellCompletionDocument(Document):
    name = 'OgWellCompletion'

    class Index:
        name = 'Og_Well_Completion'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = OgWellCompletion
        fields = [

            'created_at',
            'oil_gas_code',
            "district_no",
            "lease_no",
            "well_no",
            "district_name",
            "county_name",
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
        ]


@registry.register_document
class OgSummaryOnShoreLeaseDocument(Document):
    name = "OgSummaryOnShoreLease"

    class Index:
        name = 'Og_Summary_OnShoreLease'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = OgSummaryOnShoreLease
        fields = [

            'created_at',
            'oil_gas_code',
            "district_no",
            "lease_no",
            "operator_no",
            "field_no",
            "field_name",
            "district_name",
            "lease_name",
            "operator_name",
            "cycle_year_month_min",
            "cycle_year_month_max",
        ]


@registry.register_document
class OgSummaryMasterLarge(Document):
    name = 'OgSummaryMasterLarge'

    class Index:
        name = 'Og_Summary_Master_Large'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = OgSummaryMasterLarge
        fields = [

            'created_at',
            'oil_gas_code',
            'district_no',
            'lease_no',
            'operator_no',
            'field_no',
            'field_name',
            'district_name',
            'lease_name',
            'operator_name',
            'cycle_year_month_min',
            'cycle_year_month_max',
        ]


@registry.register_document
class OgRegulatoryLeaseDwDocument(Document):
    name = 'OgRegulatoryLeaseDw'

    class Index:
        name = 'Og_Regulatory_Lease_Dw'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = OgRegulatoryLeaseDw
        fields = [

            'created_at',
            'oil_gas_code',
            'district_no',
            'lease_no',
            'operator_no',
            'field_no',
            'field_name',
            'district_name',
            'lease_name',
            'operator_name',
            'well_no',
            'lease_off_sched_flag',
            'lease_severance_flag',
        ]


@registry.register_document
class OgOperatorDwDocument(Document):
    name = "OgOperatorDw"

    class Index:
        name = 'Og_Operator_Dw'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = OgOperatorDw
        fields = [

            'created_at',
            'operator_no',
            'operator_name',
            'p5_status_code',
            'p5_last_field_dt',
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
        ]


@registry.register_document
class OgOperatorCycleDocument(Document):
    name = 'OgOperatorCycle'

    class Index:
        name = 'Og_Operator_Cycle'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = OgOperatorCycle
        fields = [

            'created_at',
            'operator_no',
            'cycle_year',
            'cycle_month',
            'cycle_year_month',
            'operator_name',
            'oper_oil_prod_vol',
            'oper_gas_prod_vol',
            'oper_cond_prod_vol',
            'oper_csgd_prod_vol',
        ]


@registry.register_document
class OgLeaseCycleDispDocument(Document):
    name = 'OgLeaseCycleDisp'

    class Index:
        name = 'Og_LeaseCycle_Disp'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = OgLeaseCycleDisp
        fields = [

            'created_at',
            'oil_gas_code',
            'district_no',
            'lease_no',
            'operator_no',
            'field_no',
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
            'district_name',
            'lease_name',
            'operator_name',
            'field_name',
        ]


@registry.register_document
class OgLeaseCycleDocument(Document):
    name = 'OgLeaseCycle'

    class Index:
        name = 'Og_Lease_Cycle'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = OgLeaseCycle
        fields = [

            'created_at',
            'oil_gas_code',
            'district_no',
            'lease_no',
            'operator_no',
            'field_no',
            'cycle_year_month_min',
            'cycle_year_month_max',
            'district_name',
            'lease_name',
            'operator_name',
            'field_name',
        ]


@registry.register_document
class OgFieldDwDocument(Document):
    name = 'OgFieldDw'

    class Index:
        name = 'Og_Field_Dw'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = OgFieldDw
        fields = [

            'created_at',
            'field_no',
            'field_name',
            'district_no',
            'district_name',
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
        ]


@registry.register_document
class OgDistrictCycleDocument(Document):
    name = 'OgDistrictCycle'

    class Index:
        name = 'Og_District_Cycle'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = OgDistrictCycle
        fields = [

            'created_at',
            'district_no',
            'district_name',
            'cycle_year',
            'cycle_month',
            'cycle_year_month',
            'dist_oil_prod_vol',
            'dist_gas_prod_vol',
            'dist_cond_prod_vol',
            'dist_csgd_prod_vol',
        ]


@registry.register_document
class OgFieldCycleDocument(Document):
    name = 'OgFieldCycle'

    class Index:
        name = 'Og_Field_Cycle'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = OgFieldCycle
        fields = [

            'created_at',
            'field_no',
            'field_name',
            'district_no',
            'district_name',
            'cycle_year',
            'cycle_month',
            'cycle_year_month',
            'field_oil_prod_vol',
            'field_gas_prod_vol',
            'field_cond_prod_vol',
            'field_csgd_prod_vol',
        ]


@registry.register_document
class OgCountyCycleDocument(Document):
    name = 'OgCountyCycle'

    class Index:
        name = 'Og_County_Cycle'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = OgCountyCycle
        fields = [

            'created_at',
            'county_no',
            'district_no',
            'district_name',
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
            'county_name',
            'oil_gas_code',
        ]


@registry.register_document
class GpDistrictDocument(Document):
    name = 'GpDistrict'

    class Index:
        name = 'Gp_District'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = GpDistrict
        fields = [

            'created_at',
            'district_no',
            'district_name',
            'office_phone_no',
            'office_location',
        ]


@registry.register_document
class GpDateRangeCycleDocument(Document):
    name = 'GpDateRangeCycle'

    class Index:
        name = 'Gp_Date_Range_Cycle'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = GpDateRangeCycle
        fields = [

            'created_at',
            'oldest_prod_cycle_year_month',
            'newest_prod_cycle_year_month',
            'newest_sched_cycle_year_month',
            'gas_extract_date',
            'oil_extract_date',
        ]


@registry.register_document
class GpCountyDocument(Document):
    name = 'GpCounty'

    class Index:
        name = 'Gp_County'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = GpCounty
        fields = [

            'created_at',
            'county_no',
            'district_name',
            'county_name',
            'county_fips_code',
            'district_no',
            'on_shore_flag',
            'onshore_assc_cnty_flag',
        ]


@registry.register_document
class OgCountyLeaseCycleDocument(Document):
    name = 'OgCountyLeaseCycle'

    class Index:
        name = 'Og_County_Lease_Cycle'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = OgCountyLeaseCycle
        fields = [

            'created_at',
            'oil_gas_code',
            'district_no',
            'lease_no',
            'cycle_year',
            'cycle_month',
            'county_no',
            'operator_no',
            'field_no',
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
            'district_name',
            'lease_name',
            'operator_name',
            'field_name',
            'county_name',
        ]