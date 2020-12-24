from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from users import views as user_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('situmon.urls')),
    path('markdownx/', include('markdownx.urls')), #markdown用
    path('accounts/', include('allauth.urls')),
    path('profile/', user_view.UserProfileView.as_view(), name="profile"),
    path('change/', user_view.UserChangeView.as_view(), name="change"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)