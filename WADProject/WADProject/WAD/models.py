from django.db import models
from django.utils import timezone

# Create your models here.
class LogMessage(models.Model):
    name = models.CharField(max_length=100)
    plan = models.TextField()
    log_date = models.DateTimeField()
    def to_dict(self):
        return { 'id': self.id, 'name': self.name, 'plan': self.plan}
        
    def __str__(self):
        return "id: " + str(self.id)+", name: " + self.name+ "plan: " + self.plan

