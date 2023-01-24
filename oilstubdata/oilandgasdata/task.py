import logging
from time import sleep
from pathlib import Path

import pandas as pd
from celery import shared_task

from django.core.files.storage import FileSystemStorage

from oilandgasdata.core.business_logic.save_oilstub_data import (
    get_table_name_from_file_name,
    get_model_data
)


@shared_task
def upload_oilstub(path, file_name):

    sleep(10)

    storage = FileSystemStorage()
    path_object = Path(path)

    table_name = get_table_name_from_file_name(file_name)
    try:
        model = get_model_data(table_name)
        df = pd.read_csv(path_object, sep="}", header=0).to_dict('records')
        for item in df:
            item = {k.lower(): v for k, v in item.items()}
            instance = model(**item)
            instance.save()
            logging.info(f'upload data {item.values()} to {model}')
    except ValueError:
        logging.info(f"The file you upload is not yet handle")

    storage.delete(file_name)
