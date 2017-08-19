from django.db import models


class Schedule(models.Model):
    startTime = models.TimeField()
    endTime = models.TimeField()

    def __unicode__(self):
        return str(self.startTime) + " " + str(self.endTime)

    def __str__(self):
        return str(self.startTime) + " " + str(self.endTime)

    class Meta:
        verbose_name = "Schedule"
        verbose_name_plural = "Schedules"
