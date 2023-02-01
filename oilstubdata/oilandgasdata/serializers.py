import hashlib

from django.core.files import File
from django.core.files.storage import FileSystemStorage

from rest_framework import serializers

from oilandgasdata.core.business_logic.search_oilstub_data import SearchData
from oilandgasdata.task import upload_oilstub


class UploadFileSerializer(serializers.Serializer):
    upload_file = serializers.FileField(required=True)

    def create(self, validated_data):
        storage = FileSystemStorage()
        upload_file = self.validated_data.get('upload_file')

        storage.save(upload_file.name, File(upload_file))

        return upload_oilstub.delay(path=storage.path(upload_file.name), file_name=upload_file.name)


class SearchSerializer(serializers.Serializer):
    search_term = serializers.CharField(max_length=200)

    def save(self):
        search_data = SearchData(self.validated_data.get("search_term", ''))
        return search_data.search_on_agolia()
