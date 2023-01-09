from django.shortcuts import render
from django.views.generic import View, TemplateView
from inventory.models import Stock
from transactions.models import SaleBill, PurchaseBill
from firebase_admin.messaging import Message, Notification
# from pushy.api import send_message as ps_send_msg
from fcm_django.models import FCMDevice

# message = Message(
#     notification=Notification(title="title", body="text", image="url"),
#     topic="Optional topic parameter: Whatever you want",
# )

# # You can still use .filter() or any methods that return QuerySet (from the chain)
device = FCMDevice.objects.all().first()
print(device)
# send_message parameters include: message, dry_run, app

from fcm_django.models import FCMDevice
def send_notification(user_id, title, message, data):
    try:
        device = FCMDevice.objects.filter(user=user_id).last()
        result = device.send_message(title=title, body=message, data=data, 
           sound=True)
        return result
    except:
        pass

class HomeView(View):
    template_name = "home.html"
    # ps_send_msg("abcdefgh", "Hello World")
    def get(self, request):        
        labels = []
        data = []        
        stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
        for item in stockqueryset:
            labels.append(item.name)
            data.append(item.quantity)
        sales = SaleBill.objects.order_by('-time')[:3]
        purchases = PurchaseBill.objects.order_by('-time')[:3]
        context = {
            'labels'    : labels,
            'data'      : data,
            'sales'     : sales,
            'purchases' : purchases
        }
        return render(request, self.template_name, context)

class AboutView(TemplateView):
    send_notification(user_id=1, title="Order Return", message="your message", data=None)
    template_name = "about.html"

def homepage(request):
    return render(request, 'homepage.html')

def register(request):
    return render(request, 'register.html')
