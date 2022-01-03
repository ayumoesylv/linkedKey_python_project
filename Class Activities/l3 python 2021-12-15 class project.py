from Stack import Stack
from Queue import Queue

# Question 28: Use Queue (Q) to scan Stack (S) to see if it contains an element x
# given that you return the elements back to S in the original order.

Q = Queue()
S = Stack()
x = ':)'

# elements
S.push(1)
S.push(2)
S.push(':)')
S.push(3)
S.push(4)

print(S.elements)


def find_x():
    while True:
        popped_elem = S.pop()
        Q.en_queue(popped_elem)
        if popped_elem == x:
            return True
        return False


def return_to_stack():
    Q.elements = Q.elements[::-1]
    deq_elem = Q.de_queue
    for i in range(0, Q.size()):
        S.push(deq_elem)
    print(S)


# output

if find_x():
    print("Stack S contains the specified element.")

if not find_x():
    print("Stack S does not contain the specified element.")
