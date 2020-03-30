from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response

from eshopapp.serializers import ProductListSerializer, ProductRetrieveSerializer, UserInfoSerializer, \
    UserProfileSerializer, UserSerializer, CategoryListSerializer, ManufacturerListSerializer
from eshopapp.models import Product, UserProfile, Category, Manufacturer


# Create your views here.

class UserInfoView(APIView):
    """
    basic user info
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        user = self.request.user
        serializer = UserInfoSerializer(user)
        return Response(serializer.data)


class UserProfileRUView(generics.RetrieveUpdateAPIView):
    """
    user profile info
    """
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        user = self.request.user
        obj = UserProfile.objects.get(user=user)
        return obj


class UserCreateView(generics.CreateAPIView):
    """
    User Creat
    """
    serializer_class = UserSerializer


class ProductListView(generics.ListAPIView):
    """
    Product list
    """
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_class = (permissions.AllowAny,)
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ('category', 'manufacturer', 'created', 'sold', 'price')
    search_fields = ('description', 'model')
    ordering = ('id',)
    pagination_class = LimitOffsetPagination


class ProductListByCategoryView(generics.ListAPIView):
    """
    product list by category
    """
    serializer_class = ProductListSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ('category', 'manufacturer', 'created', 'sold', 'stock', 'price',)
    search_fields = ('description',)
    ordering = ('id',)

    def get_queryset(self):
        category = self.request.query_params.get('category', None)

        if category is not None:
            queryset = Product.objects.filter(category=category)
        else:
            queryset = Product.objects.all()

        return queryset


class ProductListByCategoryManufacturerView(generics.ListAPIView):
    """
    product list by manufacturer
    """
    serializer_class = ProductListSerializer
    permission_class = (permissions.AllowAny,)
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ('category', 'manufacturer', 'created', 'sold', 'stock', 'price',)
    search_fields = ('description',)
    ordering = ('id',)

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        manufacturer = self.request.query_params.get('manufacturer', None)

        if category is not None:
            queryset = Product.objects.filter(category=category, manufacturer=manufacturer)
        else:
            queryset = Product.objects.all()

        return queryset


class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductRetrieveSerializer
    permission_classes = (permissions.AllowAny,)


class CategoryListView(generics.ListAPIView):
    """
    Category list
    """
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_class = (permissions.AllowAny,)


class ManufacturerListView(generics.ListAPIView):
    """
    Manufacturer list
    """
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerListSerializer
    permission_class = (permissions.AllowAny,)


@api_view(['GET', ])
def api_root(request, format=None):
    return Response({'product_list': reverse('product_list', request=request, format=format),
                     'product_list_by_category': reverse('productlistbycategory', request=request, format=format),
                     'product_list_by_category_manufacturer': reverse('product_list_by_category_manufacturer',
                                                                      request=request, format=format),
                     # 'product_retrieve': reverse('product_retrieve', request=request, format=format),
                     'user_info': reverse('user_info', request=request, format=format),
                     # 'user_profile_ru': reverse('user_profile_ru', request=request, format=format),
                     'category_list': reverse('category_list', request=request, format=format),
                     'manufacturer_list': reverse('manufacturer_list', request=request, format=format),
                     })
