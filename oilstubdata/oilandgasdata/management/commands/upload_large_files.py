from django.core.files.storage import FileSystemStorage
from django.core.management.base import BaseCommand

from oilandgasdata.task import upload_oilstub


class Command(BaseCommand):
    help = "upload files in the system"

    def handle(self, *args, **options):
        storage = FileSystemStorage()
        file_name = "OG_FIELD_CYCLE_DATA_TABLE.dsv"
        print(storage.path(file_name))
        upload_oilstub.delay(path=storage.path(file_name), file_name=file_name)
