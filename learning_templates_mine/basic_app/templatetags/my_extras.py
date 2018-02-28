from django import template

register=template.Library()

@register.filter(name='cut_string')

def cut_string(value,arg):
    """
    this cuts all values of 'arg' from string
    """
    return value.replace(arg,'')\

#register.filter('cut_string',cut_string)
