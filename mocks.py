def msg(func):
    """only for testing
    """
    def wrap(*args, **kwargs):
        from random import randint
        res = "This is msg %d" % randint(0, 100)
        return res
    
    return wrap
