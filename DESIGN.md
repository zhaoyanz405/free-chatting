# Glossary

## Channel

In our cases, channel is a place where people send message to or fetch messages from, even just two people (obviously it support more people).

# Command Line Interface
To suppport use this chat tool in shell environment, a well-designed command line interface is required. A preliminary design will be documented in here.

## Startup

This tools should be started with a shell command, like,
```bash
$ fc start or fc join <channel-id>
```
`fc` stands for our product `free-chatting`, `join` means to join a channel, then start a conversation.

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

## Ideas

### support to switch channel

Same with the title.

### hide the history
We could add a special command or shortcut, to hide the history quickly. It would be useful when we don't want others know what we did when he approached. 

# Module Interface

## Core interface

The most important interfaces are, 
- send_to
- recv_from

Obviously, `send_to` is to send a msg to the person you want to talk or the channel.
`recv_from` is to recieve msg from which person or channel. It also reveals that the user must know what he/she is doing.

![work process](/assets/design.drawio.png)
