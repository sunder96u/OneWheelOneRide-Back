from django.urls import path
from . import views

urlpatterns = [
    path('products', views.ProductList.as_view(), name='product_list'),
    path('trails', views.Traillist.as_view(), name='trail_list'),
    path('groups', views.GroupList.as_view(), name='group_list'),
    path('products/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('trails/<int:pk>', views.TrailDetail.as_view(), name='trail_detail'),
    path('groups/<int:pk>', views.GroupDetail.as_view(), name='group_detail'),
    path('productreviews', views.ProductReviewList.as_view(), name='product_review_list'),
    path('trailreviews', views.TrailReviewList.as_view(), name='trail_review_list'),
    path('productreviews/<int:pk>', views.ProductReviewDetail.as_view(), name='product_review'),
    path('trailreviews/<int:pk>', views.TrailReviewDetail.as_view(), name='trail_review'),
    path('carts/<int:pk>', views.CartDetail.as_view(), name='card_detail'),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name='comment_detail'),
    path('users', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('login', views.Login.as_view(), name='login'),
    path('register', views.UserCreate.as_view(), name='register')
    

]