chat with your friends in shell

# v0.0.1

我们将在v0.1初步支持chat功能。具体方案设想如下，

- 使用redis作为云端存储。
- 使用redis-client作为客户端。
- 所有消息借助redis进行存取。

## 消息存取设计

由于消息具有时序性。因此考虑使用队列进行存储。
通过两个key存储对话双方的消息。例如

user1向发送消user2息
```bash
> RPUSH user2-channel msg from user1
```
user1接收消息
```bash
> LPOP user1-channel
```

# v0.0.2

通过redis命令进行消息收取，虽然勉强能够达到需求，但是实在太不方便了。因此，考虑增加命令行客户端，并提供以下接口，
```bash
$ fc join <channel-id>
> hello
(from your friend) hello!
> how are you
(from your friend) excellent!
> bye!
> \quit
$ 
```