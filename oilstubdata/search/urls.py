

from django.urls import path

from search import views

from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(
    r'api/v2/search', basename='search',
    viewset=views.GpCountySearchView
)
urlpatterns = router.urls