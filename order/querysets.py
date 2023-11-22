from datetime import datetime

from django.db.models import QuerySet, Sum, F
from django.db.models.functions import Round
from django.utils.timezone import make_aware

class OrderQuerySet(QuerySet):
    def by_customer(self, customer):
        return self

    def total_price(self):
        """ return total price of a queryset """
        total_price = self.all().annotate(
            price_sum=Round(Sum(F('orderitem__product__price')*F('orderitem__quantity')), 2)
        ).aggregate(sum=Sum("price_sum"))["sum"]
        return total_price

    def total_price_by_customer(self, customer):
        """ return total price of a queryset by a specific customer """
        total_price = self.filter(customer=customer).annotate(
            price_sum=Round(Sum(F('orderitem__product__price')*F('orderitem__quantity')), 2)
        ).aggregate(sum=Sum("price_sum"))["sum"]
        return total_price

    def submitted_in_date(self, date_value):
        """ will return a filtered queryset of a queryset for a specific date """
        return self.filter(date=make_aware(datetime.strptime(date_value, '%Y-%m-%d')))
