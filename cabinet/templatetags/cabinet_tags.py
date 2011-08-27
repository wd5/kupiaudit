from django import template
register = template.Library()

@register.filter
def cut_http(value):
    return value[7:-1]