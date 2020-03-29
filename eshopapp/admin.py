from django.contrib import admin

# Register your models here.


from eshopapp.models import Product, Category, Manufacturer, UserProfile, DeliveryAddress

from django.contrib.auth.models import User


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'mobile_phone', 'nickname', 'user', ]


admin.site.register(UserProfile, UserProfileAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]


admin.site.register(Category, CategoryAdmin)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]


admin.site.register(Manufacturer, ManufacturerAdmin)



#
# class CategoryFilter(admin.SimpleListFilter):
#     # readable title
#     title = 'Category'
#
#     # Parameter name displayed in the url, such as ?keyword=xxx.
#     parameter_name = 'category'
#
#     """
#    Customize the parameter tuples that need to be filtered.
#     """
#
#     def lookups(self, request, model_admin):
#         return (
#             ('1', 'laptop'),
#             ('2', 'tablet'),
#         )
#
#     def queryset(self, request, queryset):
#         """
#         Call self.value() to get the parameters in the url, and then filter the desired queryset.
#         """
#         if self.value() == '1':
#             return queryset.filter(id__eshopapp_product_category__category_id='1')
#         if self.value() == '2':
#             return queryset.filter(id__category='2')


class ProductAdmin(admin.ModelAdmin):
    def show_category(self, obj):
        return [ctg.name for ctg in obj.category.all()]

    show_category.short_description = 'Category'

    list_display = ['id', 'model', 'price', 'manufacturer', 'sold',
                    'show_category',
                    ]
    filter_horizontal = ['category', ]
    list_editable = ['price', 'sold', ]
    list_filter = ['manufacturer',
                   # CategoryFilter,
                   # 'product_category'
                   ]


admin.site.register(Product, ProductAdmin)


class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'contact_person', 'contact_mobile_phone', 'delivery_address', ]


admin.site.register(DeliveryAddress, DeliveryAddressAdmin)

