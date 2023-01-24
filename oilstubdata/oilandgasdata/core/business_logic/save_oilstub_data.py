import abc
from typing import List, Any

from django.apps import apps


def get_apps_models() -> List:
    return [model.__name__ for model in apps.get_app_config('oilandgasdata').get_models()]


def get_model_data(model):
    AppModel = apps.get_model('oilandgasdata', model)
    return AppModel


def get_table_name_from_file_name(file_name):
    table_name = file_name.strip(".csv").lower().split("_")[:-1]
    return "".join([name.capitalize() for name in table_name])


class SaveDataToDatabase:
    model: Any

    @abc.abstractmethod
    def execute(self):
        ...
