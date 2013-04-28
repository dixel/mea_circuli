import collections

def pp(data):
    pretty_print(data, 0)

def pretty_print(res, indent):
    if isinstance(res, unicode):
        print " " * indent + res.encode('utf-8')
    elif isinstance(res, dict):
        print " " * indent + "{"
        p = dict(map(lambda x: pretty_print(x, indent + 4), res.iteritems()))
        print " " * indent + "}"
        return p
    elif isinstance(res, tuple):
        print " " * indent + "("
        p = list(map(lambda x: pretty_print(x, indent + 4), res))
        print " " * indent + ")"
        return p
    elif isinstance(res, list):
        print " " * indent + "["
        p = list(map(lambda x: pretty_print(x, indent + 4), res))
        print " " * indent + "]"
        return p
    else:
        print " " * indent + str(res)
