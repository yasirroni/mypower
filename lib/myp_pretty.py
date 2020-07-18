def myp_pretty(value, htchar='\t', lfchar='\n', indent=0):
    '''This is pretty printer function.
    Edited from y.petremann [answer](https://stackoverflow.com/a/26209900).
    '''
    nlch = lfchar + htchar * (indent + 1)
    if type(value) is dict or value.__class__.__name__ == 'Struct':
        items = [
            nlch + repr(key) + ': ' + myp_pretty(value[key], htchar, lfchar, indent + 1)
            for key in value
        ]
        return '{%s}' % (','.join(items) + lfchar + htchar * indent)
    elif type(value) is list:
        items = [
            nlch + myp_pretty(item, htchar, lfchar, indent + 1)
            for item in value
        ]
        return '[%s]' % (','.join(items) + lfchar + htchar * indent)
    elif type(value) is tuple:
        items = [
            nlch + myp_pretty(item, htchar, lfchar, indent + 1)
            for item in value
        ]
        return '(%s)' % (','.join(items) + lfchar + htchar * indent)
    else:
        return repr(value)