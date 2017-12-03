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

@register.filter
def genDOM(value, arg):
    config = value[arg] if arg != None else value
    DOM = ('<' + config['label'] if 'label' in config else '')
    DOM += (' id="' + config['id'] + '"') if 'id' in config else ''
    DOM += (' name="' + config['name'] + '"') if 'name' in config else ''
    if 'elements' in config:
        for key, val in config['elements'].items():
            DOM += (' ' + key + '="' + val + '"')
    DOM += '>' if 'label' in config else ''
    if 'value' in config and type(config['value']) == list:
        for each in config['value']:
            DOM += genDOM(each,  None)
    else:
        DOM += config['value'] if 'value' in config else ''
    DOM += ('</' + config['label'] + '>') if 'label' in config else ''
    return DOM
