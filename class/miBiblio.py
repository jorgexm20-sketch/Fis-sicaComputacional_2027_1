import numpy as np

def cubo(x):
    """Funcion para elevar un numero al cubo."""
    
    return x**3

def cuad(x):
    """Funcion para elevar un numero al cuadrado.
    Funciona siempre y cuando el tipo de x permita la multiplicacion.
    """
    return x*x

def distancia(r,theha,z):
    """" 
    Esta función calcula la distancia entre un punto 
    p dado en coordenadas cilindricas y el origen """

    return np.sqrt(r**2 + z**2)

def factorial(n):
    """Esta función genera el factorial de un numero n"""
    n = int(n)
    
    if n<0:
        f = "Tu numero Es menor que 0 intenta con otro"

    elif n == 0:
        f = 1 
    elif n> 0:
        f = 1
        for i in range(1,n+1):
            f = i* f 
    return f


def factorial_recursivo(n):
    n = int(n)
    if n == 0:
        n = 1
        return n  
    elif n>0:
        return n * factorial_recursivo(n-1)


def catalan(n):
    
    if n == 0:
        c_n = 1
        return c_n
    elif n>0:
        c_n = 1
        for i in range(1,n+1):

            c_n = ((4*i-2)*c_n)//(i+1)
        return c_n

def catalan_recursivo(n):
    if n == 0:
        
        return 1
    elif n>0:
        
        return ((4*n-2)*catalan_recursivo(n-1))//(n+1)

def g(m, n):
    if n == 0:
        return m
    else:
        return g(n, m % n)

def factores_primos(n):
    factores = []
    i = 2

    while i <= n:
        if n % i == 0:
            factores.append(i)
            n = n // i
        else:
            i += 1

    return factores