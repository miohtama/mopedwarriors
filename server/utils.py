from StringIO import StringIO

def convert_from_camelcase_to_underscore(str):
    """
    :param str: aStringLikeThis
    
    :return: a_string_like_this
    """
    
    buf = StringIO()
    for c in str:
        if c.isupper():
            c = c.lower()
            buf.write("_")
            buf.write(c)
        else:
            buf.write(c)
            
    return buf.getvalue()
    