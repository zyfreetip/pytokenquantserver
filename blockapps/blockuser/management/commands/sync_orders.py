from django.core.management.base import BaseCommand
from oscar.apps.order.models import Order
from oscar.apps.basket.models import Basket
from blockuser.models import QuantPolicyOrder
import logging
from django.utils import timezone

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        orders = Order.objects.filter()
        for order in orders:
            date_placed = order.date_placed
            user = order.user
            basket = order.basket
            lines = order.lines
            for line in lines.all():
                product = line.product
                quantity = line.quantity
                policy_id = product.id
                quantorders = QuantPolicyOrder.objects.filter(user=user, policy_id=policy_id)
                for quantorder in quantorders:
                    if quantorder.policy_end_time > date_placed:
                        quantorder.policy_end_time += timezone.timedelta(days=30*quantity)
                    else:
                        quantorder.policy_start_time = date_placed
                        quantorder.policy_end_time = date_placed + timezone.timedelta(days=30*quantity)
                    quantorder.save()
                if not quantorders:
                    policy_end_time = date_placed + timezone.timedelta(days=30*quantity)
                    QuantPolicyOrder.objects.create(user=user, policy_id=policy_id, \
                                                     policy_start_time=date_placed,
                                                     policy_end_time=policy_end_time)   
            import ipdb;ipdb.set_trace()
           