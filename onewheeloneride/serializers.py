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
    group = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='group_detail'
    )
    class Meta:
        model = Group
        fields = ('id', 'name', 'description', 'picture', 'group')

class UserIdSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='user_detail'
    )
    class Meta:
            model = User
            fields = ('id', 'user')

class ProductIdSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='product_detail'
    )
    class Meta:
        model = Product
        fields = ('id' , 'product')

class TrailIdSerializer(serializers.HyperlinkedModelSerializer):
    trail = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='trail_detail'
    )
    class Meta:
        model = Trail
        fields = ('id', 'trail')

class GroupIdSerializer(serializers.HyperlinkedModelSerializer):
    group = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='group_detail'
    )
    class Meta:
            model = Group
            fields = ('id', 'group')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer()
    model = ModelSerializer()
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'picture', 'category', 'model')

class ProductReviewSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductIdSerializer()
    user = UserIdSerializer()
    class Meta:
        model = ProductReview
        fields = ('id', 'rating', 'review', 'user', 'product')

class TrailReviewSerializer(serializers.HyperlinkedModelSerializer):
    trail = TrailIdSerializer()
    user = UserIdSerializer()
    class Meta:
        model = TrailReview
        fields = ('id', 'rating','review', 'user', 'trail')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    group = GroupIdSerializer()
    user = UserIdSerializer()
    class Meta:
        model = Comment
        fields = ('id', 'date', 'comment', 'user', 'group')