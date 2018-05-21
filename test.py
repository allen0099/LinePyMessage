"""This is a demo for test what operation Line will sent when
I do some action, it can test all OpTypes.
"""

from linepy import *
from secret_class import *


def receive_message(operation):
    print(operation)


if __name__ == '__main__':
    line = LINE(line_token)
    oepoll = OEPoll(line)

    oepoll.addOpInterruptWithDict({
        OpType.RECEIVE_MESSAGE: receive_message
    })

    while True:
        oepoll.trace()
