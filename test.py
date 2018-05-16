from linepy import *
from secret_class import *

line = LINE(line_token)
oepoll = OEPoll(line)


def receive_message(operation):
    print(operation)


oepoll.addOpInterruptWithDict({
    OpType.RECEIVE_MESSAGE: receive_message
})

if __name__ == '__main__':
    while True:
        oepoll.trace()
