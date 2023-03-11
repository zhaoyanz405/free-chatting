def string(max_length=10):
    """only for testing

    Args:
        max_length (int): the length of the string to generated

    """

    def deco(func):
        def wrap(*args, **kwargs):
            import random

            res = ""
            for i in range(random.randint(0, max_length)):
                res += random.choice('abcdefghijklmnopqrstuvwxyz ')  # include the space

            return res

        return wrap

    return deco
