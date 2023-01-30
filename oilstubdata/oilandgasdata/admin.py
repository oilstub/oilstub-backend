from django.contrib import admin

from oilandgasdata.models import (
    OgWellCompletion,
    OgSummaryOnShoreLease,
    OgSummaryMasterLarge,
    GpCounty,
    GpDistrict,
    OgCountyCycle,
    OgCountyLeaseCycle,
    OgDistrictCycle,
    OgFieldCycle,
    OgFieldDw,
    OgOperatorCycle,
    OgOperatorDw,
    OgRegulatoryLeaseDw,
)

# Register your models here.
admin.site.register(OgWellCompletion)
admin.site.register(OgSummaryOnShoreLease)
admin.site.register(OgSummaryMasterLarge)
admin.site.register(GpCounty)
admin.site.register(GpDistrict)
admin.site.register(OgCountyCycle)
admin.site.register(OgCountyLeaseCycle)
admin.site.register(OgDistrictCycle)
admin.site.register(OgFieldCycle)
admin.site.register(OgFieldDw)
admin.site.register(OgOperatorCycle)
admin.site.register(OgOperatorDw)
admin.site.register(OgRegulatoryLeaseDw)
