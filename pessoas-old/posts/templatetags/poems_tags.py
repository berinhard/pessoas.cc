from django.template import Library
from django.utils.safestring import mark_safe

register = Library()


def format_phrase(phrase):
    splitted_phrase = phrase.split(' ')
    formatted_phrase = ''

    for splitted_item in splitted_phrase:
        if splitted_item == '':
            splitted_item = '&ensp;'
        else:
            splitted_item = splitted_item + ' '
        formatted_phrase = formatted_phrase + splitted_item

    return formatted_phrase


@register.filter()
def enspify(value):
    splitted_text = value.split('\n')
    formatted_text = ''

    for phrase in splitted_text:
        if phrase.startswith(' '):
            phrase = format_phrase(phrase)
        formatted_text = formatted_text + phrase

    return mark_safe(formatted_text)


@register.filter()
def populate_embedded(poem):
    emb = '<iframe src="%s" frameborder="0" allowfullscreen></iframe>'
    return emb % poem.resource_url
