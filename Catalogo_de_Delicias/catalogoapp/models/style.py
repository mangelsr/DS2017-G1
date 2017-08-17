from django.db import models
from .choices import fonts

class Style(models.Model):
    color = models.CharField(max_length=7)
    font = models.CharField(choices=fonts, max_length=30)
    size = models.IntegerField()

    def __unicode__(self):
        return self.font + " " + str(self.size) + " " + self.color
    
    def __str__(self):
        return self.font + " " + str(self.size) + " " + self.color
    
    class Meta:
        verbose_name = "Style"
        verbose_name_plural = "Styles"