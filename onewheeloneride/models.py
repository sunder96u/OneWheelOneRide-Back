from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    profile_picture = models.CharField(max_length=250)

    def __str__(self):
        return self.email
    
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='OneWheel')

    def __str__(self):
        return self.name
    
class Model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='OneWheel')

    def __str__(self):
        return self.name
        
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=250)
    qantity = models.IntegerField(default=1)
    description = models.TextField(default='No Description Given')
    price = models.FloatField(default=0)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    model_id = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Trail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=250)
    address = models.CharField(max_length=100)
    difficulty = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class ProductReview(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5)
    review = models.TextField(default='No Review Given')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id
    
class TrailReview(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    trail_id = models.ForeignKey(Trail, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5)
    review = models.TextField(default='No Review Given')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id
    
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.IntegerField(default=0)
    subtotal = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=250)
    description = models.TextField(default='No Description Given')
    members = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    comment = models.TextField(default='No Comment Given')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id



