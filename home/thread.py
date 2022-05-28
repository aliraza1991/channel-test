import threading
from .models import Student
from faker import Faker
import random
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

fake = Faker()

class CreateStudentThread(threading.Thread):
    def __init__(self, total):
        self.total = total
        threading.Thread.__init__(self)
    
    def run(self):
        try:
            
            print('thread execution started')
            channel_layer = get_channel_layer()
            current_total = 0
            for i in range(self.total):
                current_total += 1
                stud_obj = Student.objects.create(
                    name=fake.name(),
                    email=fake.email(),
                    address=fake.address(),
                    age=random.randint(10, 50)
                )
                channel_layer = get_channel_layer()
                data = {"id": current_total, "current_total": current_total, "total": self.total, "student_name": stud_obj.name, "student_email": stud_obj.email, "student_age": stud_obj.age, "student_address": stud_obj.address}
                # print(data, 'data')
                async_to_sync(channel_layer.group_send)(
                    "test_consumer2_group", {
                        'type': 'send_notification',
                        'value': json.dumps(data)
                    }
                )
        except Exception as e:
            print(e)