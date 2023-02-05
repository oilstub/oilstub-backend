import abc
from dataclasses import dataclass, field
from typing import List, Any

from django.apps import apps

from oilandgasdata.infrastructure.provider.agolia_search import SearchOilGasAdapter


def get_apps_models() -> List:
    return [model.__name__ for model in apps.get_app_config('oilandgasdata').get_models()]


def get_model_data(model):
    AppModel = apps.get_model('oilandgasdata', model)
    return AppModel


def get_table_name_from_file_name(file_name):
    table_name = file_name.strip(".").lower().split("_")[:-2]
    return "".join([name.capitalize() for name in table_name])


@dataclass
class SearchData:
    search_term: str
    params: dict = field(default_factory=lambda: {"hitsPerPage": 100})

    def search_on_agolia(self):
        # models = get_apps_models()
        app_model = get_model_data('OgDistrictCycleData')
        agolia_search = SearchOilGasAdapter(self.search_term, app_model, self.params).execute()
        return {'OgDistrictCycleData': agolia_search}
        # output = {}
        # for model in models:
        #     app_model = get_model_data(model)
        #     agolia_search = SearchOilGasAdapter(self.search_term, app_model, self.params).execute()
        #     output.update({model: agolia_search})
        # return output
