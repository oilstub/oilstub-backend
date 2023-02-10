from search import views

from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(
    r'api/v1/gp-county-search', basename='gp-county-search',
    viewset=views.GpCountySearchView
)
router.register(
    r'api/v1/gp-county-filter', basename='gp-county-filter',
    viewset=views.GpCountyFilterView
)
router.register(
    r'api/v1/gp-county-autocomplete', basename='gp-county-autocomplete',
    viewset=views.GpCountyCompletionView
)

urlpatterns = router.urls
