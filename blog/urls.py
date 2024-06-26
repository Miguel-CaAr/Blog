from django.contrib import admin
from django.urls import path, include
# Doc
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# Viewset
from categories.api.router import router_categories
from posts.api.router import router_post
from comments.api.router import router_comments

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="Documentacion de la api del blog",
        terms_of_service="",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    #    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('api/', include('users.api.router')),
    path('api/', include(router_categories.urls)),
    path('api/', include(router_post.urls)),
    path('api/', include(router_comments.urls)),
    path('api/', include('utils.password_reset.api.router'))
]
