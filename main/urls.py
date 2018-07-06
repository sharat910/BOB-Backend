from django.urls import path, include
from .routers import router
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^', include('django.contrib.auth.urls')),
    path(r'api/', include(router.urls)),
    path(r'rest-auth/', include('rest_auth.urls')),
    path(r'rest-auth/registration/', include('rest_auth.registration.urls'))
]
