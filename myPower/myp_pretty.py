def myp_pretty(value, htchar=' ', width=4, lfchar='\n', indent=0):
    '''This is pretty printer function.
    Edited from y.petremann [answer](https://stackoverflow.com/a/26209900).
    '''
    nlch = lfchar + htchar * width * (indent + 1)
    if type(value) is dict or value.__class__.__name__ == 'Struct':
        items = [
            nlch + repr(key) + ': ' + myp_pretty(value[key], htchar, width, lfchar, indent + 1)
            for key in value
        ]
        return '{%s}' % (','.join(items) + lfchar + htchar * width * indent)
    elif type(value) is list:
        items = [
            nlch + myp_pretty(item, htchar, width, lfchar, indent + 1)
            for item in value
        ]
        return '[%s]' % (','.join(items) + lfchar + htchar * width * indent)
    elif type(value) is tuple:
        items = [
            nlch + myp_pretty(item, htchar, width, lfchar, indent + 1)
            for item in value
        ]
        return '(%s)' % (','.join(items) + lfchar + htchar * width * indent)
    else:
        return repr(value)