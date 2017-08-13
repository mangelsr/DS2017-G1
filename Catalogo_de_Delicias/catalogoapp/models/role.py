from django.db import models

class Role(models.Model):
    name = models.TextField(max_length=50)
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"