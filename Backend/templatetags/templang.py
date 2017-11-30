from django import template

register = template.Library()

@register.filter
def underscore(value, arg):
    return value['_' + str(arg)]
