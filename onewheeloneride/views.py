from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Login(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductReviewList(generics.ListAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer

class ProductReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer

class Traillist(generics.ListAPIView):
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer

class TrailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer

class TrailReviewList(generics.ListAPIView):
    queryset = TrailReview.objects.all()
    serializer_class = TrailReviewSerializer

class TrailReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrailReview.objects.all()
    serializer_class = TrailReviewSerializer

class CartList(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TrailReviewCreate(generics.CreateAPIView):
    queryset = TrailReview.objects.all()
    serializer_class = TrailReviewSerializer

class ProductReviewCreate(generics.CreateAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer

class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class GroupMembers(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    

