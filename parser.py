from stonks import get_stocks

def validate_message(msg):
    msg = msg.split()
    if len(msg) < 2:
        return False

    if msg[0] not in ['stocks', 'stockbot', 'stonks']:
        return False

    return True

def list_price(command, msg):
    msg_spl = msg.split()

    if len(msg_spl) != 3:
        return f"Error: 'stockbot {command} <symbol>"

    stonks = msg_spl[0]
    command_name = msg_spl[1]
    symbol = msg_spl[2]

    # TODO: Really this shouldn't be here... we should handle this way better..
    # but I was feeling lazy and this gets the job done
    try:
        current_price = get_stocks(symbol)
    except:
        return f"Unable to find information for: '{symbol}'"

    return f'current price for {symbol}: ${current_price}'

###############################################################################
#   All supported commands can be specified in this dict.  For each command,
#   the command name is expected to point to a function that accepts two
#   arguments: The name of the command and the message provided by the user.
#
#   Realistically based on the way it is implemented right now, the message is
#   the only argument you really need, but accepting the command as an argument
#   allows for more flexibility in the future (if the position of the command
#   becomes variable).
###############################################################################
commands = {
    "list_price": list_price,
    "help": lambda cmd, msg: "Choose from:\n" + "\n".join(commands.keys())
}

def parse_message(msg):
    """
        It is expected that the message argument to this function has already
        been validated.
    """
    command = msg.split()[1]

    if command not in commands:
        return f"Invalid command '{command}'"

    return commands[command](command, msg)

if __name__ == '__main__':
    inp = ""
    while inp != 'quit':
        try:
            inp=input(">>> ")
        except KeyboardInterrupt:
            break

        if not validate_message(inp):
            print("Invalid message")
            continue

        print("\n" + parse_message(inp) + "\n")

    print("\nGoodbye!")
