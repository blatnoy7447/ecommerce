from os import name
from django.urls import path
from django.conf.urls.static import static
from ecommerce import settings
from mainapp import AdminViews,views


urlpatterns = [
    path('admin_login_process/',views.adminLoginProcess,name="admin_login_process"),
    path('admin_logout_process/',views.adminLogoutProcess,name="admin_logout_process"),

    # PAGE FOR ADMIN
    path('admin_home/',AdminViews.admin_home,name='admin_home'),
    
    #CATEGORIES
    path('category_list',AdminViews.CategoriesListView.as_view(),name="category_list"),
    path('category_create',AdminViews.CategoriesCreate.as_view(),name="category_create"),
    path('category_update/<slug:pk>',AdminViews.CategoriesUpdate.as_view(),name="category_update"),

    #SUBCATEGORIES
    path('sub_category_list',AdminViews.SubCategoriesListView.as_view(),name="sub_category_list"),
    path('sub_category_create',AdminViews.SubCategoriesCreate.as_view(),name="sub_category_create"),
    path(
        'sub_category_update/<slug:pk>',
        AdminViews.SubCategoriesUpdate.as_view(),
        name="sub_category_update"
    ),

    #MERCHANT USER
    path('merchant_create',AdminViews.MerchantUserCreateView.as_view(),name="merchant_create"),
    path('merchant_list',AdminViews.MerchantUserListView.as_view(),name="merchant_list")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(
    settings.STATIC_URL,document_root=settings.STATICFILES_DIRS
)

