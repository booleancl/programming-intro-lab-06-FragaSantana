
#funsión no retorna
def Saludo():
    print('Hola como estas?')
Saludo()

#funsión valores de retorno
def Sum(a,b):
    return a + b

Resultado = Sum(5,7)
print('La suma es = ', Resultado)

#función parámetros por defecto
def Resta(c=0,d=0):
    return(c - d)

ResulRest = Resta(3)
print('La resta es = ',ResulRest)    
