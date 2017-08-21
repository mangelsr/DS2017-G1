from django.db import models
from .choices import *

class Style(models.Model):
    color = models.CharField(choices=colors, max_length=20)
    font = models.CharField(choices=fonts, max_length=30)

    def __unicode__(self):
        return self.font + " " + self.color

    def __str__(self):
        return self.font + " "  + self.color

    class Meta:
        verbose_name = "Style"
        verbose_name_plural = "Styles"
