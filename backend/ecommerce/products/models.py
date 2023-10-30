from django.db import models
from users.models import User

class Product(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, default= 1)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    stock = models.PositiveIntegerField()
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    thumbnail = models.URLField()
    class Meta:
	    db_table = "product"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.URLField()

    def __str__(self):
        return f"Image for {self.product.title}"


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
	    db_table = "cart"
