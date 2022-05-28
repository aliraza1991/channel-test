from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import JsonResponse
import json
from .thread import *
import time

def home(request):
    # for i in range(0, 2):
    #     channel_layer = get_channel_layer()
    #     data = {"count": i}
    #     await (channel_layer.group_send)(
    #         "test_consumer2_group", {
    #             'type': 'send_notification',
    #             'value': json.dumps(data)
    #         }
        # )
        # time.sleep(1)
    return render(request, 'home.html', {'msg': "Home"})

def generate_student_data(request):
    
    total = request.GET.get('total')
    CreateStudentThread(int(total)).start()
    return JsonResponse({"status": 200})
