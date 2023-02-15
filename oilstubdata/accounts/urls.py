from django.urls import path, include
from accounts.views import SignUpAPI, SignInAPI, MainUser
from knox import views as knox_views

urlpatterns = [
    path('auth/', include('knox.urls')),
    path('auth/register/', SignUpAPI.as_view()),
    path('auth/login/', SignInAPI.as_view()),
    path('auth/user/', MainUser.as_view()),
    path('auth/logout/', knox_views.LogoutView.as_view(), name="knox-logout"),
]
