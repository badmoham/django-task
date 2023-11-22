from django.db.models import QuerySet, Sum


class CustomerQuerySet(QuerySet):
    def annotate_with_total_spending(self):
        return self.annotate(total_spending=Sum("order__total_price"))

    def annotate_with_order_count(self):
        return self