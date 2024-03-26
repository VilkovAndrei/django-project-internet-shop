from django import template

from catalog.models import Product

register = template.Library()

@register.filter()
def as_table(model):
    ret = ""
    for name in model._meta.get_fields():
        try:
            field = str(getattr(model, name))
            if field:
                ret += '<tr><td class="name">'+name+'</td><td class="field">'+field+'</td></td>'
        except AttributeError:
            pass
    return ret