

from django.urls import path

from search.views import GpCountySearchView


urlpatterns = [
    path('api/v2/search/<str:query>/', GpCountySearchView.as_view()),
]
