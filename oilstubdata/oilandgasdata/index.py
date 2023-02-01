import algoliasearch_django as algoliasearch

from oilandgasdata.models import(
    OgWellCompletion,
    OgSummaryOnShoreLease,
    OgSummaryMasterLarge,
    GpCounty,
    GpDistrict,
    GpDateRangeCycle,
    OgCountyCycle,
    OgCountyLeaseCycle,
    OgDistrictCycle,
    OgFieldCycle,
    OgFieldDw,
    OgOperatorCycle,
    OgOperatorDw,
    OgRegulatoryLeaseDw,
)

# algoliasearch.register(OgCountyLeaseCycle)
# algoliasearch.register(OgSummaryOnShoreLease)
# algoliasearch.register(OgWellCompletion)
# algoliasearch.register(OgSummaryMasterLarge)
# algoliasearch.register(GpCounty)
# algoliasearch.register(GpDistrict)
# algoliasearch.register(OgCountyCycle)
algoliasearch.register(OgDistrictCycle)
# algoliasearch.register(OgFieldCycle)
# algoliasearch.register(OgFieldDw)
# algoliasearch.register(OgOperatorCycle)
# algoliasearch.register(OgOperatorDw)
# algoliasearch.register(OgRegulatoryLeaseDw)
