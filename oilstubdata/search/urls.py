from search import views

from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(
    r'api/v1/gp-county-search', basename='gp-county-search',
    viewset=views.GpCountySearchView
)
router.register(
    r'api/v1/search/og-well-completion', basename='og-well-completion',
    viewset=views.OgWellCompletionDocumentViewSet
)

router.register(
    r'api/v1/search/og-summary-onShore-lease', basename='og-summary-onShore-lease',
    viewset=views.OgSummaryOnShoreLeaseDocumentViewSet
)

router.register(
    r'api/v1/search/og-summary-master-large', basename='og-summary-master-large',
    viewset=views.OgSummaryMasterLargeViewSet
)

router.register(
    r'api/v1/search/og-regulatory-lease', basename='og-regulatory-lease',
    viewset=views.OgRegulatoryLeaseDwDocumentViewSet
)
urlpatterns = router.urls
