from search import views

from rest_framework.routers import SimpleRouter


router = SimpleRouter()

router.register(r'v1/search/gp-county-search', basename='gp-county-search', viewset=views.GpCountySearchView)
router.register(
    r'v1/search/og-well-completion', basename='og-well-completion',
    viewset=views.OgWellCompletionDocumentViewSet
)

router.register(
    r'v1/search/og-summary-onShore-lease', basename='og-summary-onShore-lease',
    viewset=views.OgSummaryOnShoreLeaseDocumentViewSet
)

router.register(
    r'v1/search/og-summary-master-large', basename='og-summary-master-large',
    viewset=views.OgSummaryMasterLargeViewSet
)

router.register(
    r'v1/search/og-regulatory-lease', basename='og-regulatory-lease',
    viewset=views.OgRegulatoryLeaseDwDocumentViewSet
)

router.register(
    r'v1/search/og-regulatory-dw', basename='og-regulatory-dw',
    viewset=views.OgOperatorDwDocumentViewSet
)

router.register(
    r'v1/search/og-operator-cycle', basename='og-operator-cycle',
    viewset=views.OgOperatorCycleDocumentViewSet
)

router.register(
    r'v1/search/og-lease-cycle-disp', basename='og-lease-cycle-disp',
    viewset=views.OgLeaseCycleDispDocumentViewSet
)

router.register(r'v1/search/og-field-dw', basename='og-field-dw', viewset=views.OgFieldDwDocumentViewSet)

router.register(
    r'api/v1/search/og-district-cycle', basename='og-district-cycle',
    viewset=views.OgDistrictCycleDocumentViewSet
)

router.register(r'api/v1/search/og-field-cycle', basename='og-field-cycle', viewset=views.OgFieldDwDocumentViewSet)

router.register(
    r'api/v1/search/og-county-cycle', basename='og-county-cycle',
    viewset=views.OgCountyCycleDocumentViewSet
)

router.register(r'api/v1/search/gp-district', basename='gp-district', viewset=views.GpDistrictDocumentViewSet)
router.register(
    r'api/v1/search/gp-date-range-cycle', basename='gp-date-range-cycle', viewset=views.GpDateRangeCycleDocumentViewSet
)
router.register(
    r'api/v1/search/og-county-lease-cycle', basename='og-county-lease-cycle',
    viewset=views.OgCountyLeaseCycleDocumentViewSet
)
router.register(r'v1/search/og-lease-cycle', basename='og-lease-cycle', viewset=views.OgLeaseCycleDocumentViewSet)
