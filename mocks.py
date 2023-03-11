def string(max_length):
    """only for testing

    Args:
        channel (_type_): _description_

    """
    def deco(func):
        def wrap(*args, **kwargs):
            import random
            
            res = ""
            for i in range(random.randint(0, max_length)):
                res += random.choice('abcdefghijklmnopqrstuvwxyz ') # include the space

            return res
        
        return wrap
    
    return deco
