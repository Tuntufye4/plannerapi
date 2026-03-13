from django.db import models   

class ShoppingItem(models.Model):
    item_name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bought = models.BooleanField(default=False)      
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):      
        return self.item_name                              