from django.db import models

# Create your models here.
class Products(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=20)
    desc=models.CharField(max_length=300)
    # category=models.CharField(max_length=50, default="")
    # publish_date=models.DateField()
    photo=models.ImageField(upload_to="images/", blank=True, null=True ,default="")

    def __str__(self):
        return self.product_name





# product_id=models.AutoField
#     product_name=models.CharField(max_length=20)
#     desc=models.CharField(max_length=300)
#     category=models.CharField(max_length=50, default="")
#     publish_date=models.DateField(default="")
#     photo=models.ImageField(upload_to="images/", blank=True, null=True ,default="")

# class Product_sub_cat(models.Model):
#     sab_cat=models.CharField(max_length=100)
#     def __str__(self):
#         return self.sab_cat


class Productcat(models.Model):
    prodcat=models.CharField(max_length=100)
    # sab_cat=models.ForeignKey(Product_sub_cat, on_delete=models.CASCADE)
    prod_cat_desc=models.TextField()
    photo=models.ImageField(upload_to="images/", blank=True, null=True ,default="")
    def __str__(self):
        return self.prodcat


class Productsitems(models.Model):
    product_id=models.AutoField
    prodcat=models.ForeignKey(Productcat, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=20)
    desc=models.TextField()
    prize=models.FloatField()
    photo=models.ImageField(upload_to="images/", blank=True, null=True ,default="")
    sale=models.BooleanField(default=False)
    top_sale=models.BooleanField(default=False)

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    current_user=models.IntegerField()
    prod_details=models.ForeignKey(Productsitems,on_delete=models.CASCADE)
    quantity=models.IntegerField()

    def __str__(self):
        return str(self.prod_details)
