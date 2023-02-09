from dataclasses import dataclass

from elasticsearch_dsl import Q


@dataclass
class ElasticSearchQuery:
    search_term: str

    def generate_q_expression(self):
        q = Q(
            'bool',
            should=[
                Q('match', oil_gas_code=self.search_term),
                Q('match', district_no=self.search_term),
                Q('match', lease_no=self.search_term),
                Q('match', county_no=self.search_term),
                Q('match', operator_no=self.search_term),
                Q('match', field_no=self.search_term),
                Q('match', gas_well_no=self.search_term),
                Q('match', district_name=self.search_term),
                Q('match', lease_name=self.search_term),
                Q('match', operator_name=self.search_term),
                Q('match', field_name=self.search_term),
                Q('match', county_name=self.search_term),
                Q('match', county_fips_code=self.search_term),
                Q('match', on_shore_flag=self.search_term),
                Q('match', onshore_assc_cnty_flag=self.search_term),
                Q('match', office_location=self.search_term),
                Q('match', field_class=self.search_term),
                Q('match', well_no=self.search_term),
            ],
            fuzziness='auto'
        )
        return q
