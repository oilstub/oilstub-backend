from django.core.files.storage import FileSystemStorage
from django.core.management.base import BaseCommand

from oilandgasdata.task import upload_oilstub


class Command(BaseCommand):
    help = "upload files in the system"

    def handle(self, *args, **options):
        storage = FileSystemStorage()
        file_names = [
            "OG_SUMMARY_MASTER_LARGE_DATA_TABLE.dsv", "OG_SUMMARY_ONSHORE_LEASE_DATA_TABLE.dsv",
            "OG_WELL_COMPLETION_DATA_TABLE.dsv"
        ]
        for file_name in file_names:
            print(storage.path(file_name))
            upload_oilstub.delay(path=storage.path(file_name), file_name=file_name)
