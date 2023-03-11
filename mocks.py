def msg(func):
    """only for testing

    Args:
        channel (_type_): _description_

    """
    def wrap(*args, **kwargs):
        from random import randint
        res = "This is msg %d" % randint(0, 100)
        return res
    
    return wrap
