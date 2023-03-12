import mocks
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def create() -> str:
    """Create a channel

    Returns:
        str: channel-id
    """

def send(channel, msg):
    """Send msg to a channel

    Args:
        channel (string): channel id
        msg (string): message
    """
    r.rpush(channel, msg)


@mocks.msg
def recv(channel, timeout):
    """fetch msg from a channel

    Args:
        channel (string): channel id
        timeout (int): time limit for tje fetching
    """
    msg = r.blpop(channel, timeout=timeout)
    if msg:
        return msg[1].decode('utf-8')
    else:
        return None
