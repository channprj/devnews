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
    path('users/', include('users.urls')),
    path('links/', include('links.urls')),
]

admin.site.site_header = _('Devnews 관리자 대시보드')
admin.site.site_title = _('Devnews 관리자 대시보드')
admin.site.index_title = _('Devnews 관리자 대시보드')
