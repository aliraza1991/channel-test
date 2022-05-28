from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.TextField()
    is_seen = models.BooleanField(default=False)


    def __str__(self):
        return self.user.first_name

    
    def save(self, *args, **kwargs):
        channel_layer = get_channel_layer()
        obj = Notification.objects.filter(is_seen=False).count()
        data = {"count": obj, "current_notification": self.notification}
        async_to_sync(channel_layer.group_send)(
            "test_consumer_group", {
                'type': 'send_notification',
                'value': json.dumps(data)
            }
        )
        super(Notification, self).save(*args, **kwargs)