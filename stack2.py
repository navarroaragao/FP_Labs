def new():
    return ''
    
def push(x, s):
    if isinstance(x, int) and x >= 0 and isinstance(s, str):
        return s+'12'+(''.join(str(ord(c)) for c in str(x)))
    else:
        print('Argumento inválido (push).')
        
def pop(s):
    if isinstance(s, str) and len(s)>1:
        r = s[:]
        while(r[-2:]!='12'):
            r = r[:-2]
        return r[:-2]
    else:
        print('Argumento inválido (pop).')

def top(s):
    if isinstance(s, str) and len(s) > 1:
        aux = s[:]
        r = 0
        while(aux[-2:]!='12'):
            r = r*10+int(chr(int(aux[-2:])))
            aux = aux[:-2]
        return r   
    else:
        print('Argumento inválido (top).')
        
def is_empty(s):
    if isinstance(s, str):
        return s == '' 
    else:
        print('Argumento inválido (is_empty).')
        
def clone(s):
    if isinstance(s, str):
        return s[:]
    else:
        print('Argumento inválido (is_empty).')