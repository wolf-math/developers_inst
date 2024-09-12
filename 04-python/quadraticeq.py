
def quadratic_eq(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)

    det = b ** 2 - (4 * a * c)

    if det < 0:
        return 'No real solution'
    
    den = 2*a
    if det == 0:
        print('1 solution')
        print(b**2 /den)
    else:
        print ((b**2 - det)/den, (b**2 + det)/den)