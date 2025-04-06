from django import template

register = template.Library()

@register.filter
def color(value):
    green = int(100 + (sum(value.name.encode('ascii')) % 100))
    red = int(sum(value.description.encode('ascii')) % (green / 3))
    blue = int(sum(value.city.encode('ascii')) % (green / 3))
    return '#{:02X}{:02X}{:02X}'.format(red, green, blue)