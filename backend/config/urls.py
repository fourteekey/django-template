from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from api.views import index_view              # VUE or another JS frontend


# Swagger Header
schema_view = get_schema_view(openapi.Info(title="ProjectName", default_version='v1'), url=settings.API_URL)


urlpatterns = [
    # Django Admin
    # path('admin/', admin.site.urls),

    # http://127.0.0.1:8000/swagger/
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # API VIEWS
    # http://127.0.0.1:8000/api/v1/
    path('api/v1/', include('api.api')),

    # http://127.0.0.1:8000/
    # re_path('lk/.*$', index_view, name='lk'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
