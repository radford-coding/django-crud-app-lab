from django import template

register = template.Library()

@register.filter
def color(value):
    green = int(50 + sum(value.name.encode('ascii')) % 100)
    red = int(sum(value.description.encode('ascii')) % (green / 2))
    blue = int(sum(value.city.encode('ascii')) % (green / 2))
    return '#{:02X}{:02X}{:02X}'.format(red, green, blue)
    # return 90

@register.filter
def color_green(value):
    return 30 + sum(value.name.encode('ascii')) % 120

@register.filter
def color_red(value):
    return sum(value.description.encode('ascii')) % 30

@register.filter
def color_blue(value):
    return sum(value.city.encode('ascii')) % 30