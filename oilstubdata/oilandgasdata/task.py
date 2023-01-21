from time import sleep
from celery import shared_task
from .models import ProductImage
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from pathlib import Path


@shared_task
def upload_oilstub(import_id, path, file_name):

    sleep(10)

    storage = FileSystemStorage()

    path_object = Path(path)

    with path_object.open(mode='rb') as file:
        picture = File(file, name=path_object.name)

        instance = ProductImage(product_id=import_id, image=picture)

        instance.save()

    storage.delete(file_name)
