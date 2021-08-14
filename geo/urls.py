from django.urls import path
from .apiviews import ProviderViewSet, ServiceAreaViewSet, PolygonViewSet, ServicesList, UserCreate, LoginView
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register('providers', ProviderViewSet, base_name='providers')
router.register(r'providers/(?P<provider_pk>[^/.]+)/polygons', ServiceAreaViewSet, base_name='polygons')
router.register(r'providers/(?P<provider_pk>[^/.]+)/polygons/(?P<polygon_pk>[^/.]+)/polygon', PolygonViewSet, base_name='polygon')

schema_view = get_swagger_view(title='ServiceArea API')

urlpatterns = [
    path("services/", ServicesList.as_view(), name="polygon_services"), # Create new user
    path("users/", UserCreate.as_view(), name="user_create"), # Create new user
    path("login/", LoginView.as_view(), name="login"), # Login
    path(r'swagger-docs/', schema_view),
    path(r'docs/', include_docs_urls(title='Polls API'))
]

urlpatterns += router.urls

