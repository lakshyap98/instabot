from django import template

register = template.Library()

from ..models import Product

@register.simple_tag
def Posts_features():
    return Product.objects.all().count()

@register.inclusion_tag('product_list.html')
def latest_products(count=2):
    # import pdb; pdb.set_trace()
    latest = Product.objects.all()[:count]
    return {'obj':latest}

# @register.assignment_tag
# def questions_list(count=2):
#     from polls.models import Poll
#     qs = Poll.objects.all()
#     return qs