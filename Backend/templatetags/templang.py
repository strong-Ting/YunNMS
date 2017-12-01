from copy import deepcopy
from django import template

register = template.Library()

@register.filter
def underscore(value, arg):
    try:
        return value['_' + str(arg)]
    except:
        return 'Error/Backend/templatetags/templang/underscore'

@register.filter
def get(value, arg):
    try:
        _value = deepcopy(value)
        del _value[arg]
        return _value
    except:
        return 'Error/Backend/templatetabs/templang/remove'

@register.filter
def dictGet(value, arg):
    try:
        return value[str(arg)] if arg in value else 'None'
    except:
        return 'Error/Backend/templatetags/templang/dictGet'
