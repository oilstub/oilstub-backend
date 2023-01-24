from django.contrib import admin

from oilandgasdata.models import (
    OgWellCompletionData,
    OgSummaryOnShoreLeaseData,
    OgSummaryMasterLargeData,
    GpCountyData,
    GpDistrictData,
    OgCountyCycleData,
)

# Register your models here.

admin.site.register(OgWellCompletionData)
admin.site.register(OgSummaryOnShoreLeaseData)
admin.site.register(OgSummaryMasterLargeData)
admin.site.register(GpCountyData)
admin.site.register(GpDistrictData)
admin.site.register(OgCountyCycleData)
