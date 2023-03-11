import mocks


def send(channel, msg):
    """Send msg to a channel

    Args:
        channel (string): channel id
        msg (string): message
    """


@mocks.string(30)
def recv(channel, timeout):
    """fetch msg from a channel

    Args:
        channel (string): channel id
        timeout (int): time limit for fetching
    """