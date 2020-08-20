from django.db import models
from django.utils.timezone import now


class RoastBoastModel(models.Model):
    is_boast = models.BooleanField()
    content = models.CharField(max_length=280)
    up_vote = models.IntegerField()
    down_vote = models.IntegerField()
    submit_time = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.content
