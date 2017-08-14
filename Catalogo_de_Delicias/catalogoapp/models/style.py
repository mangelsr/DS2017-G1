from django.db import models

class Style(models.Model):
    color = models.TextField(max_length=7)
    font = models.TextField()
    size = models.IntegerField()

    def __unicode__(self):
        return self.font + " " + str(self.size) + " " + self.color
    
    def __str__(self):
        return self.font + " " + str(self.size) + " " + self.color
    
    class Meta:
        verbose_name = "Style"
        verbose_name_plural = "Styles"