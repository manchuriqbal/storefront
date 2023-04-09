from django.db import models

# Create your models here.

class Promotions(models.Model):
    description= models.CharField(max_length=255)
    discount= models.FloatField()


class Collection(models.Model):
    title= models.CharField(max_length=255)
    featured_product= models.ForeignKey('Product', on_delete=models.SET_NULL, null= True, related_name='+')


class Product(models.Model):
    title= models.CharField(max_length=255)
    slug= models.SlugField()
    desc=models.TextField()
    unit_price=models.DecimalField(max_digits=6, decimal_places=2)
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
    collection=models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions=models.ManyToManyField(Promotions)

class Customer(models.Model):
    MEMBERSHIP_BRONZE="B"
    MEMBERSHIP_SILVER="S"
    MEMBERSHIP_GOLD="G"

    MEMBERSHIP_CHOICES=[
        (MEMBERSHIP_BRONZE, "Bronze"),
        (MEMBERSHIP_SILVER, "Silver"),
        (MEMBERSHIP_GOLD, "Gold")
    ]
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=255)
    bithdate=models.DateField(null=True)
    membership=models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    


class Order(models.Model):
    PAYMENT_STATUS_PENDING= "P"
    PAYMENT_STATUS_COMPLETE= "C"
    PAYMENT_STATUS_FAILED= "F"


    PAYMENT_STATUS=[
        (PAYMENT_STATUS_PENDING, "Pending"),
        (PAYMENT_STATUS_COMPLETE, "Complete"),
        (PAYMENT_STATUS_FAILED, "Failed")
    ]
    
    placed_at=models.DateTimeField(auto_now_add=True)
    payment= models.CharField(max_length=1, choices=PAYMENT_STATUS, default=PAYMENT_STATUS_PENDING)
    customer=models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product= models.ForeignKey(Product, on_delete=models.PROTECT)
    quentity=models.PositiveIntegerField()
    unit_price= models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    zip_code= models.IntegerField(default=1, blank=True, null=True)
    customer= models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)


class Cart(models.Model):
    create_at= models.DateTimeField(auto_now=True)

class CartItem( models.Model):
    cart= models.ForeignKey(Cart, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quntity=models.PositiveSmallIntegerField()

