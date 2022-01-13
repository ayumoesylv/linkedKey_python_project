from Stack import Stack
from collections import deque

def move_stacks(S, T):
    buffer = deque()

    while S.size() > 0:
        buffer.appendleft(S.pop())

    while T.size() > 0:
        buffer.appendleft(T.pop())

    print(buffer)


S = Stack()
T = Stack()
S.push(1)
S.push(2)
S.push(3)
T.push('A')
T.push('B')
T.push('C')

move_stacks(S, T)

