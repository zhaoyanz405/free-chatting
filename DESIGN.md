# Command Line Interface
To suppport use this chat tool in shell environment, a well-designed command line interface is required. A prelimatery design will be documented in here.

## Startup

This tools should be started with a shell command, like,
```bash
$ fc start or fc join <channel-id>
```
`fc` stands for our product `free-chatting`, `join` means to join a channel to start a conversation.

## Interactive terminal
after joinning the channel, a interactive terminal should be activate. just like the `redis-cli` behaved.

```bash
# friendA's termimal
$ fc join example-channel
joined success! 
(exmaple-channel) _
(exmaple-channel) Hello
send success (or error msg)
(exmaple-channel) (friendB) Hi!
(example-channel) _
```

In another side, once your friend logged in,
```bash
# friendB's terminal
$ fc join example-channel
joined success! 
(exmaple-channel) (friendA) Hello
(example-channel) Hi!
send success (or error msg)
(example-channel) _
```
