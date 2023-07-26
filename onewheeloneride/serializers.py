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
          
class TrailReviewSerializer(serializers.HyperlinkedModelSerializer):
    review = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='review_detail'
    )
    class Meta:
        model = TrailReview
        fields = ('id', 'rating','review', 'user')

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

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    comment = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='comment_detail'
    )
    class Meta:
        model = Comment
        fields = ('id', 'date', 'comment', 'trail')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    group = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='group_detail'
    )
    class Meta:
        model = Group
        fields = ('id', 'name', 'description', 'picture', 'group')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category_id = CategorySerializer()
    model_id = ModelSerializer()
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'picture', 'category_id', 'model_id')

class ProductReviewSerializer(serializers.HyperlinkedModelSerializer):
    review = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='review_detail'
    )
    class Meta:
        model = ProductReview
        fields = ('id', 'rating', 'review', 'product')