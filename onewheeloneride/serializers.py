from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='category_detail'
    )
    class Meta:
        model = Category
        fields = ('id', 'name', 'category')

class ModelSerializer(serializers.HyperlinkedModelSerializer):
    models = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='model_detail'
    )
    class Meta:
        model = Model
        fields = ('id', 'name','models')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='users_detail'
    )
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'users', 'password')

class LoginSerializer(serializers.HyperlinkedModelSerializer):
    users_id = UserSerializer(
        many=True,
        read_only=True,
    )
    class Meta:
        model = User
        fields = ('id','email', 'users_id', 'password')

class TrailSerializer(serializers.HyperlinkedModelSerializer):
    trail = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='trail_detail'
    )
    class Meta:
        model = Trail
        fields = ('id', 'name', 'address', 'difficulty', 'picture', 'trail')

class CartSerializer(serializers.HyperlinkedModelSerializer):
    cart = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='cart_detail'
    )
    class Meta:
        model = Cart
        fields = all

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    members = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    class Meta:
        model = Group
        fields = ('id', 'name', 'description', 'picture', 'members')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category_id = CategorySerializer()
    model_id = ModelSerializer()
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'picture', 'category_id', 'model_id')

class ProductReviewSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta:
        model = ProductReview
        fields = ('id', 'review', 'rating', 'user_id', 'product_id')

class TrailReviewSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    trail_id = serializers.PrimaryKeyRelatedField(queryset=Trail.objects.all())
    class Meta:
        model = TrailReview
        fields = ('id', 'review', 'rating', 'user_id', 'trail_id')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    group_id = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())
    class Meta:
            model = Comment
            fields = ('id', 'comment', 'user_id', 'group_id')


