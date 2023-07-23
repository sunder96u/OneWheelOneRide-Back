from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='users_detail'
    )
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'users')
    
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='products_detail'
    )
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'picture', 'products')

class ProductReviewSerializer(serializers.HyperlinkedModelSerializer):
    review = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='review_detail'
    )
    class Meta:
        model = ProductReview
        fields = ('id', 'rating', 'review', 'product')
        
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