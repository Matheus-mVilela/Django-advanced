import datetime
from django import template

register = template.Library()


@register.simple_tag
def footer_msg():
    return 'Dajngo advanced 2.0x'


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)
