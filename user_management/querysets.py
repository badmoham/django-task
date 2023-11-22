from django.db.models import QuerySet, Sum, Count


class CustomerQuerySet(QuerySet):
    def annotate_with_total_spending(self):
        """ will return the queryset with annotated values for each customer's total spending """
        return self.annotate(total_spending=Sum("order__total_price"))

    def annotate_with_order_count(self):
        """ will return the queryset with annotated values for each customer's total order count """
        return self.annotate(order_count=Count("order"))
