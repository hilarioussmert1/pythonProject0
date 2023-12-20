from django import template

register = template.Library()

CURRENCIES_SYMBOLS = {
    'rub': '₽',
    'usd': '$',
}


@register.filter()
def currency(value, code='rub'):
    """
   value: значение, к которому нужно применить фильтр
   """
    postfix = CURRENCIES_SYMBOLS[code]

    return f'{value} {postfix}'


bad_words = [
    'редиска',
    'круто',
    'собака',
]


@register.filter()
def censor(value):
    for word in bad_words:
        value = value.lower().replace(word.lower(), '***')
    return f'{value}'
