import time
import queue
import threading
import traceback

import click

from msg import send, recv



@click.group()
def cli():
    pass

@click.command()
@click.argument("channel")
def join(channel):
    interactive_terminal(channel)

cli.add_command(join)

def recv_loop(channel, q, event):
    while not event.is_set():
        msg = recv(channel)
        if not msg:
            time.sleep(1)
            continue

        q.put(msg)
        time.sleep(1) # for testing


def interactive_terminal(channel):
    """open a terminal for inputs and outputs

    Args:
        channel (string): channel id
    """
    print("openning a termimal, waiting for joinning the channel.")
    print('Joined success. ^.^ \n')

    msg_q = queue.Queue()
    e = threading.Event()

    t_recv = threading.Thread(target=recv_loop, args=(channel, msg_q, e))
    t_recv.start()

    try:
        while True:
            while not msg_q.empty():
                print(msg_q.get())

            msg = input(">>> ")
            if msg == 'exit' or msg.startswith('\q'):
                break

            send(channel, msg)

    except Exception as e:
        print(traceback.format_exc())
        print("meeting some issues. would you want restart again? (y/n)")
        if input(">>> ") == 'y':
            interactive_terminal(channel)

    print("closing the terminal")
    e.set()
    t_recv.join()
    print("closed.")
    exit(0)


if __name__ == "__main__":
    cli()