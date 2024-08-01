from py_currency_converter import convert

def change_currency(base, final, value):

    dict = convert(base=base, amount=value, to=[final])

    for curr in dict:
        return(dict[curr])

