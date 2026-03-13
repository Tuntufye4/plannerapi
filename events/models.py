from django.db import models     

class EventItem(models.Model):
    event_name = models.CharField(max_length=200)
    item_name = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):    
        return f"{self.event_name} - {self.item_name}"                 