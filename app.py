def gordon(a):
    a=a.upper().replace('A','@').replace('E','*').replace('I','*').replace('O','*').replace('U','*').split(' ')

    r = []
    for i in a:
        r.append(i+'!!!!')

    return (' '.join(r))
