from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, GalleryPageView
from django.conf.urls.static import static
from ecommerce import settings
from mainapp import AdminViews


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('gallery/', GalleryPageView.as_view(), name='gallery'),

    # PAGE FOR ADMIN
    path('admin_home',AdminViews.admin_home)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(
    settings.STATIC_URL,document_root=settings.STATICFILES_DIRS
)

