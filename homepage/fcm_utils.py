from pyfcm import FCMNotification

def send_push_notification(device_token, message):
    push_service = FCMNotification(api_key="YOUR_SERVER_KEY_HERE")
    result = push_service.notify_single_device(registration_id=device_token, message_title="Push Notification", message_body=message)