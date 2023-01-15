import signal # Import the signal module from the python standard library

def handle_ctrl_c(signal, frame):
    """
    This function will be called every time the user presses ctrl+c.
    The signal argument is the signal that was received (in this case SIGINT)
    The frame argument is the current stack frame, which is not used in this example
    """
    # Put your cleanup code here
    print('Ctrl+C pressed')
    # Exit the program
    exit()

# Register handle_ctrl_c function as the handler for the SIGINT signal
signal.signal(signal.SIGINT, handle_ctrl_c)

# Put your main program code here
while True:
    print('Running...')