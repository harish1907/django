from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from your_app.models import MyUser
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from App.serializers import *
channel_layer = get_channel_layer()
import json
from .models import *
misfire_grace_time = 600
max_instances = 200

scheduler=BackgroundScheduler()

def send_data_to_socket():
    try:
        async_to_sync(channel_layer.group_send)(
            "braker_data",  
            {
                "type": "send_braker_notification",
                "instance": BrakerScreenerSerializerData(BrakerScreener.objects.filter(interval='15m')[:50],many=True).data,
            },
        )
        async_to_sync(channel_layer.group_send)(
            "braker_data",  
            {
                "type": "send_braker_notification_1h",
                "instance": BrakerScreenerSerializerData(BrakerScreener.objects.filter(interval='1h')[:50],many=True).data,
            },
        )
        async_to_sync(channel_layer.group_send)(
            "braker_data",  
            {
                "type": "send_braker_notification_4h",
                "instance": BrakerScreenerSerializerData(BrakerScreener.objects.filter(interval='4h')[:50],many=True).data,
            },
        )
        async_to_sync(channel_layer.group_send)(
            "braker_data",  
            {
                "type": "send_braker_notification_1d",
                "instance": BrakerScreenerSerializerData(BrakerScreener.objects.filter(interval='1d')[:50],many=True).data,
            },
        )
        async_to_sync(channel_layer.group_send)(
            "braker_data",  
            {
                "type": "send_braker_notification_1w",
                "instance": BrakerScreenerSerializerData(BrakerScreener.objects.filter(interval='1w')[:50],many=True).data,
            },
        )
        async_to_sync(channel_layer.group_send)(
            "braker_data",  
            {
                "type": "send_divergence_notification",
                "instance": DivergenceScreenerSerializerData(DivergenceScreener.objects.filter(interval='15m')[:50],many=True).data,
            },
        )
        async_to_sync(channel_layer.group_send)(
            "braker_data",  
            {
                "type": "send_divergence_notification_1h",
                "instance": DivergenceScreenerSerializerData(DivergenceScreener.objects.filter(interval='1h')[:50],many=True).data,
            },
        )
        async_to_sync(channel_layer.group_send)(
            "braker_data",  
            {
                "type": "send_divergence_notification_4h",
                "instance": DivergenceScreenerSerializerData(DivergenceScreener.objects.filter(interval='4h')[:50],many=True).data,
            },
        )
        async_to_sync(channel_layer.group_send)(
            "braker_data",  
            {
                "type": "send_divergence_notification_1d",
                "instance": DivergenceScreenerSerializerData(DivergenceScreener.objects.filter(interval='1d')[:50],many=True).data,
            },
        )
        async_to_sync(channel_layer.group_send)(
            "braker_data",  
            {
                "type": "send_divergence_notification_1w",
                "instance": DivergenceScreenerSerializerData(DivergenceScreener.objects.filter(interval='1w')[:50],many=True).data,
            },
        )
    except Exception as e:
        print(e)
def start_socket_job():
    return scheduler.add_job(send_data_to_socket, trigger='interval', seconds=5, misfire_grace_time=misfire_grace_time, max_instances=max_instances)


def datadelete():
    try:
        data=[]
        data+=list(BrakerScreener.objects.filter(interval='15m')[100:])
        data+=list(BrakerScreener.objects.filter(interval='1h')[100:])
        data+=list(BrakerScreener.objects.filter(interval='4h')[100:])
        data+=list(BrakerScreener.objects.filter(interval='1d')[100:])
        data+=list(BrakerScreener.objects.filter(interval='1w')[100:])
        
        data+=list(DivergenceScreener.objects.filter(interval='15m')[100:])
        data+=list(DivergenceScreener.objects.filter(interval='1h')[100:])
        data+=list(DivergenceScreener.objects.filter(interval='4h')[100:])
        data+=list(DivergenceScreener.objects.filter(interval='1d')[100:])
        data+=list(DivergenceScreener.objects.filter(interval='1w')[100:])
        for i in data:
            i.delete()
        print("deleted")
    except Exception as e:
        print(e)

def delete_scheduler():
    return scheduler.add_job(datadelete, trigger='interval', minutes=15, misfire_grace_time=misfire_grace_time, max_instances=max_instances)
