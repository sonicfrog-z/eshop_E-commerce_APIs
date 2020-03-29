from rest_framework import serializers
from django.contrib.auth.models import User
from eshopapp.models import Product, Manufacturer, Category, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'mobile_phone', 'nickname', 'description', 'icon', 'created', 'updated',)
        read_only_fields = ('user',)


class UserInfoSerializer(serializers.ModelSerializer):
    profile_of = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'profile_of',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)  # 接受前端传过来的用户名和密码
        user.set_password(validated_data['password'])  # 通过字典方式调用
        user.save()  # 保存到内存中
        user_profile = UserProfile(user=user)
        user_profile.save()
        return user


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('id', 'name',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'model', 'price', 'sold', 'category', 'manufacturer',)


class ProductRetrieveSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = (
            'id', 'model', 'image', 'price', 'sold', 'category', 'manufacturer', 'description', 'created', 'updated',)
