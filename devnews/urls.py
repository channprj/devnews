# django
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include
from django.urls import path
from django.utils.translation import gettext as _

# third-party
from rest_framework import routers

# views
from users.views import health_check
from users.views import UserViewSet
from users.views import ProfileViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profile', ProfileViewSet)
# router.register(r'check', health_check, base_name='health_check')


urlpatterns = [
    path('admin/', admin.site.urls),

    # auth
    # path('accounts/', include('django.contrib.auth.urls')), # customizable
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='admin/login.html',),
        name='login',
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        {'next_page': settings.LOGOUT_REDIRECT_URL},
        name='logout',
    ),

    # rest_framework
    path('api-auth/', include('rest_framework.urls')),
    path('check/', health_check, name='health_check'),
] + router.urls

admin.site.site_header = _('Devnews 관리자 대시보드')
admin.site.site_title = _('Devnews 관리자 대시보드')
admin.site.index_title = _('Devnews 관리자 대시보드')
