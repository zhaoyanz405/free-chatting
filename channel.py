import mocks
import redis


class RedisManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.r = redis.Redis(host='localhost', port=6379, db=0)
            cls._instance._init_available_channels()
        return cls._instance

    def _init_available_channels(self):
        """maintain a set of 0-999 as the optional channels"""
        self.r.delete('available_channel')
        self.r.sadd('available_channel', *range(1000))

    def create(self) -> str:
        """Create a channel

        Returns:
            str: channel
        """
        channel = self.r.spop('available_channel')
        if not channel:
            raise Exception('No More Available Channel')

        self.r.rpush(channel, "")

        return str(channel)

    def destroy(self, channel:str):
        """Destroy a channel

        Re-add the channel_id to available_channel
        """
        self.r.delete(channel)
        self.r.sadd('available_channel', channel)

    def send(self, channel, msg):
        """Send msg to a channel

        Args:
            channel (string): channel id
            msg (string): message
        """
        self.r.rpush(channel, msg)

    @mocks.msg
    def recv(self, channel, timeout):
        """fetch msg from a channel

        Args:
            channel (string): channel id
            timeout (int): time limit for tje fetching
        """
        msg = self.r.blpop(channel, timeout=timeout)
        if msg:
            return msg[1].decode('utf-8')
        else:
            return None

redis_manager = RedisManager()
