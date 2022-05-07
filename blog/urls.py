from django.urls import path, include
from api import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api/', views.apiOverview, name="api-overview"),
    path('api/posts/', views.post_list, name="post-list"),
    path('api/posts/<str:pk>/', views.post_detail, name="post-detail"),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('markdown/', include( 'django_markdown.urls'))
    # path('', include("posts.urls")),
    # path('', include(router.urls)),
    # path('', PostListAPIView.as_view(), name='post-list'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]