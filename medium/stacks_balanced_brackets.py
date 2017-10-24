# Find matching brackets '{}', '[]', '()'
# problem from CTCI

def is_matched(expression):

    stack = []
    opening = {'{', '[', '('}
    closing = {'}', ']', ')'}
    
    #expression = list(expression)
    
    for i in expression:
        if i in opening:
            stack.append(i)
        
        if i in closing:
            
            if stack == []:
                return False
            
            x = stack[-1]
            
            if i == ']' and x == '[':
                stack.pop(-1)
            elif i == '}' and x == '{':
                stack.pop(-1)
            elif i == ')' and x == '(':
                stack.pop(-1)
            else:
                return False
    if stack == []:
        return True
    else:
        return False
               

t = 3

expression = '{{[[(())]]}}'

if is_matched(expression) == True:
    print "YES"
else:
    print "NO"
