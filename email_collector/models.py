from django.db import models


class TimeStamp(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Subscribe(TimeStamp):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
