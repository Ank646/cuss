from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='profile_pic/CustomerProfilePic/', default='profile_pic/CustomerProfilePic/Screenshot_3.png')
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    is_active = models.BooleanField(default=False)
    # code = models.CharField(blank=True)
    token = models.CharField(default="", max_length=200)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_email(self):
        return self.user.email

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name


class Product(models.Model):
    gend = (
        ('Men', 'Men'),
        ('Women', 'Women'),

    )
    name = models.CharField(max_length=40)
    product_image = models.ImageField(
        upload_to='product_image/', null=True, blank=True)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=40)
    date = models.DateField(auto_now_add=True, null=True)
    gender = models.CharField(max_length=40, choices=gend, default="Women")
    tag1 = models.CharField(default="", max_length=40)
    tag2 = models.CharField(default="", max_length=40)

    def __str__(self):
        return self.name


class Orders(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Order Confirmed', 'Order Confirmed'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=500, null=True)
    mobile = models.CharField(max_length=20, null=True)
    order_date = models.DateField(auto_now_add=True, null=True)
    quantity = models.IntegerField(default=0)
    status = models.CharField(max_length=50, null=True, choices=STATUS)

    @property
    def get_total_price(self):
        return self.product.price*self.quantity


class Cart(models.Model):

    customer = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)

    @property
    def get_price(self):
        return self.product.price

    @property
    def get_total_price(self):
        return self.product.price*self.quantity

    @property
    def get_title(self):
        return self.product.name

    @property
    def get_image(self):
        return self.product.product_image

    @property
    def get_id(self):
        return self.product.id


class Wishlist(models.Model):

    customer = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)

    @property
    def get_price(self):
        return self.product.price

    @property
    def get_title(self):
        return self.product.name

    @property
    def get_image(self):
        return self.product.product_image

    @property
    def get_id(self):
        return self.product.id


class Feedback(models.Model):
    customer = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    rating = models.FloatField(default=1)
    feedback = models.CharField(max_length=500)
    helpful = models.IntegerField(default=0)
    unhelpful = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True, null=True)
    title = models.CharField(default="", max_length=100)

    @property
    def get_name(self):
        return self.customer.get_name


class Like(models.Model):
    customer = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    review = models.ForeignKey(
        'Feedback', on_delete=models.CASCADE, null=True)

    @property
    def get_helpful(self):
        return self.review.helpful

    @property
    def get_unhelpful(self):
        return self.review.unhelpful
