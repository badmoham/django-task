from celery import shared_task
from django.utils import timezone

from product.models import Product
from order.models import Order
from user_management.models import Manager
from utils.sms import SMS


@shared_task
def send_restock_sms():
    """ will call on SMS class send method to send a sms to managers about products """
    all_managers = Manager.objects.all()
    restock_needed = [ i.name for i in Product.objects.needs_restock()]
    total_sale = Order.objects.filter(date=timezone.now()).total_price()
    for manager in all_managers:
        msg = f"hello dear {manager.user.first_name}, \n these products need restocking: {restock_needed} \n" \
              + f" total sale: {total_sale}"
        sms = SMS(phone_number=manager.phone, message=msg)
        sms.send()
