from django.urls import path
from django.contrib import admin

from oilandgasdata import views


admin.autodiscover()


urlpatterns = [
    path(
        r'upload_files/',
        admin.site.admin_view(views.UploadOilStubDataView.as_view()),
        name='upload_files'
    )
]
