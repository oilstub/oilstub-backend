import logging
from pathlib import Path

import pandas as pd
from celery import shared_task

from django.core.files.storage import FileSystemStorage

from oilandgasdata.core.business_logic.search_oilstub_data import (
    get_table_name_from_file_name,
    get_model_data
)


def process_chunk(chunk, model):
    for item in chunk.to_dict(dict='record'):
        item = {k.lower(): v for k, v in item.items()}
        instance = model(**item)
        instance.save()
        logging.info(f'upload data {item.values()} to {model}')


@shared_task(name='upload_oilstub_data')
def upload_oilstub(path, file_name):
    storage = FileSystemStorage()
    path_object = Path(path)

    table_name = get_table_name_from_file_name(file_name)
    try:
        model = get_model_data(table_name)
        with pd.read_csv(path_object, sep="}", header=0, chunksize=1000, na_filter=False) as reader:
            for chunk in reader:
                process_chunk(chunk, model)
    except ValueError:
        logging.info(f"The file you upload is not yet handle")

    storage.delete(file_name)
