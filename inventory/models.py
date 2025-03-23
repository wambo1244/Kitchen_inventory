from django.db import models

# Supplier model
class Supplier(models.Model):
   name = models.CharField(max_length=255)
   contact = models.CharField(max_length=255, default="Unknown Contact")
   address = models.TextField()
   email = models.EmailField(default="noemail@example.com")

   def __str__(self):
        return self.name

# Ingredient model
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=50)  # e.g., grams, liters

    def __str__(self):
        return self.name

# Inventory model for tracking stock levels
class Inventory(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    expiry_date = models.DateField(null=True, blank=True)  # Expiry date for perishable items
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Price of the ingredient
    location = models.CharField(max_length=255, null=True, blank=True)  # Location in the kitchen
    category = models.CharField(max_length=100, null=True, blank=True)  # Category (e.g., grains, dairy, etc.)
    status = models.CharField(max_length=20, choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock'), ('Low Stock', 'Low Stock')], default='In Stock')
    date_added = models.DateField(auto_now_add=True)  # Date the item was added



    def __str__(self):
        return f"{self.ingredient.name} - {self.quantity} {self.ingredient.unit}"

# Order model to track stock updates or orders placed
class Order(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_ordered = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status_choices = [('Pending', 'Pending'), ('Delivered', 'Delivered')]
    status = models.CharField(max_length=10, choices=status_choices, default='Pending')

    def __str__(self):
        return f"Order for {self.ingredient.name} - {self.quantity_ordered} {self.ingredient.unit}"

