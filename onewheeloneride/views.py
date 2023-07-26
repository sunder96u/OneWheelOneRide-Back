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

class UserCreate(generics.CreateAPIView):
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

class CreateProductReview(generics.CreateAPIView):
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

class CreateTrailReview(generics.CreateAPIView):
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

class CreateComment(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class GroupList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CreateGroup(generics.CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CreateTrail(generics.CreateAPIView):
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer

# class UserLogin(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserRegister(generics.CreateAPIView): 
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


