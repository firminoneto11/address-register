
def clear_console():
    """
    This is a simple function that resets the terminal/console screen to help visualize the information.
    :return: Returns a command to reset the screen.
    """
    from os import name, system
    if name == 'nt':
        return system('cls')
    return system('clear')


def clear_pycharm():
    """
    This is a simple function that resets the terminal/console of PyCharm IDE to help visualize the information.
    :return: Returns the command set to reset the IDE terminal.
    """
    from pynput.keyboard import Key, Controller
    keyb = Controller()
    with keyb.pressed(Key.alt):
        keyb.press("'")
