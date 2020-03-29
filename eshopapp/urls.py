from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from eshopapp import views

urlpatterns = [
    url(r'^user_info/$', views.UserInfoView.as_view(), name='user_info'),
    url(r'^user_profile_ru/(?P<pk>[0-9]+)/$', views.UserProfileRUView.as_view(), name='user_profile_ru'),
    url(r'^user_create/$', views.UserCreateView.as_view(), name='user_create'),
    url(r'^product_list/$', views.ProductListView.as_view(), name='product_list'),
    url(r'^product_list_by_category/$', views.ProductListByCategoryView.as_view(), name='productlistbycategory'),
    url(r'^product_list_by_category_manufacturer/$', views.ProductListByCategoryManufacturerView.as_view(),
        name='product_list_by_category_manufacturer'),
    url(r'^product_retrieve/(?P<pk>[0-9]+)/$', views.ProductRetrieveView.as_view(), name='product_retrieve'),

    url(r'^$', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
