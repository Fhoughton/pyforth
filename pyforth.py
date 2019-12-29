#Environment
stack = []
variables = {}
funcs = {}

def eval_token(token,tokens):
    #Stack manipulation
    if token == ".":
        print(stack.pop())
    elif token == "dup":
        stack.append(stack[0])
    #Variable definitions
    elif token == "variable":
        variables[tokens[1]] = tokens[2]
        tokens.pop()
        tokens.pop()
    #Function definitions
    elif token == ":":
        variables[str(tokens[1])] = tokens[2:]
        print(tokens[1])
        tokens.clear()
    #Arithmetic operations
    elif token == "+": 
        stack.append(stack.pop()+stack.pop())
    elif token == "-":
        stack.append(stack.pop()-stack.pop())
    elif token == "*":
        stack.append(stack.pop()*stack.pop())
    elif token == "/":
        stack.append(stack.pop()/stack.pop())
    #Logical operations
    elif token == "=":
        if stack.pop() == stack.pop():
            stack.append(-1)
        else:
            stack.append(0)
    elif token == ">":
        if stack.pop() > stack.pop():
            stack.append(-1)
        else:
            stack.append(0)
    elif token == "<":
        if stack.pop() == stack.pop():
            stack.append(-1)
        else:
            stack.append(0)
    elif token == "invert":
        if stack.pop() == 0:
            stack.append(-1)
        else:
            stack.append(0)
    elif token == "quit":
        exit()
    elif str(token) in funcs:
        parse_expr(funcs[token])
        tokens.pop()
    else:
        stack.append(token)
    if len(tokens) > 0:
        tokens.pop()
    return tokens

#Takes user input, tokenizes and processes it   
def parse_expr(expr):
    tokens = expr.split()
    
    while len(tokens) > 0:
        tokens = eval_token(tokens[0],tokens)
    
#Read, eval, print loop
while True:
    parse_expr(input())
    print(stack)