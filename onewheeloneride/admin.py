from django.contrib import admin
from .models import User, Category, Model, Product, Trail, ProductReview, TrailReview, Cart, Group, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Model)
admin.site.register(Product)
admin.site.register(Trail)
admin.site.register(ProductReview)
admin.site.register(TrailReview)
admin.site.register(Cart)
admin.site.register(Group)
admin.site.register(Comment)
