from django.db import models

# ================= TASKS =================

class DailyTask(models.Model):      
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    selectedDate = models.DateField(null=True)

    def __str__(self):
        return self.title               