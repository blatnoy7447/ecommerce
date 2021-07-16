from django.urls import path
from django.conf.urls.static import static
from ecommerce import settings
from mainapp import AdminViews,views


urlpatterns = [
    path('admin_login_process/',views.adminLoginProcess,name="admin_login_process"),

    # PAGE FOR ADMIN
    path('admin_home/',AdminViews.admin_home,name='admin_home')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(
    settings.STATIC_URL,document_root=settings.STATICFILES_DIRS
)

