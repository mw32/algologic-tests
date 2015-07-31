#!/usr/bin/python

import termios, sys, os
asterisk = '*'
bkspc = '\x7f'
del_key = '\x1b'
#del_key1 = '\x08'
newlines = '\n\r'

def getkey(mask):
    c = None

    # stdin/stdout descriptors
    fd = sys.stdin.fileno()
    od = sys.stdout.fileno()

    # termios attributes
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
    new[6][termios.VMIN] = 1
    new[6][termios.VTIME] = 0
    termios.tcsetattr(fd, termios.TCSANOW, new)

    try:
        c = os.read(fd, 1)
        if c == del_key or c == bkspc:
            # backspace or del key => write backspace and whitespace
            os.write(od, '\b \b')
        elif c in newlines:
            # newline, just return
            return c
        else:
            # else just write masking chars
            os.write(od, mask)
        sys.stdout.flush()
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, old)
    return c


def getpassmask(prompt, mask='*'):
    print prompt
    passwd = ''
    while 1:
        c = getkey(mask)
        if c in '\n\r':
            break
        elif c == bkspc or c == del_key:
            # if backspace or del key, remove the char from string
            passwd = passwd[:len(passwd)-1]
        else:
            passwd = passwd + c
    return passwd

if __name__ == '__main__':
    a = getpassmask("Enter password:")
    print '\n',a
