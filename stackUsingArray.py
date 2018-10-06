def createStack():
    stack = []
    return stack
def isEmpty(stack):
    return len(stack) == 0
def push(stack,value):
    stack.append(value)
def pop(stack):
    if isEmpty(stack):
        return "Stack empty"
    return stack.pop()
st = createStack()
push(st,1)
push(st,2)
push(st,3)
print(st)
print(pop(st))