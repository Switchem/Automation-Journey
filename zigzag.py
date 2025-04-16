import time
import sys
indent = 0  # How many spaces to indent.
indentIncreaseing = True  # Whether the indentation is increasing or not.

try:
    while True:  # The main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)  # Pause for 1/10 of a second.

        if indentIncreaseing:
            # INcrease the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indentIncreaseing = False
        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreaseing = True
except KeyboardInterrupt:
    sys.exit()
