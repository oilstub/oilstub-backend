from dataclasses import dataclass

from elasticsearch_dsl import Q


@dataclass
class ElasticSearchQuery:
    search_term: str

    def generate_q_expression(self):
        q = Q(
            'multi_match',
            query=self.search_term,
            fields=[
                'oil_gas_code', 'district_no', 'lease_no', 'county_no', 'operator_no' 'field_no' 'gas_well_no',
                'district_name', 'lease_name', 'operator_name', 'field_name', 'county_name', 'county_fips_code',
                'on_shore_flag', 'onshore_assc_cnty_flag', 'office_location', 'field_class', 'well_no',
            ])
        return q


