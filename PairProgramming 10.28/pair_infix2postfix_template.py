def push(x):
    global stack
    global top
    top += 1 #top=0
    stack[top] = x #stak[0]에 "("를 넣어

def pop():
    global stack
    global top
    x = stack[top] #x=stack[0]  == (
    top -= 1 #top = 0
    return x

def precedence(c):
    if c =='+' or c == '-':
        return 1
    elif c == '*' or c =='/':
        return 2
    elif c == "^":
        return 3
    else:
        return -1

def convert(exp):
    global stack
    global top
    r = ""
    for i in range(len(exp)): #0~6
        c = exp[i] #(
        if precedence(c) > 0: #-1
            while top != -1 and +\
                precedence(stack[top]) >= precedence(c):
                r += str(pop())
            push(c)
        elif c == ')':
            x = pop()
            while x != '(':
                r += str(x)
                x = pop()
        elif c == '(':
            push(c)
        else:
            r += str(c)
    for i in range(top+1): #1번
        r += str(pop()) #r += "("
    return r



stack = []
for i in range(0,50):
    stack.append(0) #스택에 0을 50개 넣음..?
top = -1
exp = input("infilx expression: ")
print("postfix expression: ", convert(exp)) #exp = (a+b)*c