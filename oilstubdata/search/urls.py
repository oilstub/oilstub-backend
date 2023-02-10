from search import views

from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(
    r'api/v1/gp-county-search', basename='gp-county-search',
    viewset=views.GpCountySearchView
)
urlpatterns = router.urls
