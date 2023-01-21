from dataclasses import dataclass
from typing import List, Any

from django.apps import apps


def get_apps_models() -> List:
    return [model.__name__ for model in apps.get_app_config('oilandgasdata').get_models()]


def get_model_data(model):
    AppModel = apps.get_models('oilandgasdata', model)
    return AppModel


@dataclass
class SaveDataToDatabase:
    model: Any
