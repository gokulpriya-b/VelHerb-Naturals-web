from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=60)
    short_description = models.CharField(max_length=220)
    description = models.TextField(blank=True)
    ingredients = models.TextField(blank=True, help_text="Separate ingredients with commas.")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    image_key = models.CharField(max_length=80, blank=True, help_text="Fallback image filename in static/images.")
    is_featured = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name

class Order(models.Model):
    STATUS = [("new","New"),("confirmed","Confirmed"),("processing","Processing"),("shipped","Shipped"),("completed","Completed"),("cancelled","Cancelled")]
    customer_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.TextField()
    items = models.TextField(help_text="Order items summary")
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS, default="new")
    created_at = models.DateTimeField(auto_now_add=True)
    is_custom = models.BooleanField(default=False)
    def __str__(self): return f"#{self.pk} {self.customer_name}"

class CustomOrder(models.Model):
    STATUS = [("new","New"),("contacted","Contacted"),("accepted","Accepted"),("completed","Completed"),("closed","Closed")]
    customer_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    product_type = models.CharField(max_length=100)
    ingredients_requested = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=1)
    budget = models.CharField(max_length=80, blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default="new")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"Custom #{self.pk} — {self.customer_name}"
