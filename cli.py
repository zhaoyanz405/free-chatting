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


def interactive_terminal(channel):
    """open a terminal for inputs and outputs

    Args:
        channel (string): channel id
    """
    print("openning a termimal, waiting for joinning the channel.")
    print('Joined success. ^.^ \n')

    while True:
        msg = input(">>> ")
        if msg == 'exit' or msg == '\q':
            break

        send(channel, msg)
        print(recv(channel))
        


    print("The terminal closed.")


if __name__ == "__main__":
    cli()