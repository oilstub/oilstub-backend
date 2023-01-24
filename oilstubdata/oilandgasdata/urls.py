from django.urls import path

from django.contrib import admin

from oilandgasdata.views import UploadOilStubDataView


admin.autodiscover()


urlpatterns = [
    path(
        r'upload_files/',
        UploadOilStubDataView.as_view(),
        name='upload_files'
    )
]
