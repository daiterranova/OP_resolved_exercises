import operations as o


def calculator(int, int1):
    o.sumar(int, int1)
    o.restar(int, int1)
    o.multiplicar(int, int1)
    o.dividir(int, int1)
    print(f"suma: {o.sumar(int,int1)}, resta: {o.restar(int,int1)}, multiplicacion: {o.multiplicar(int,int1)}, dividir: {o.dividir(int,int1)}")


calculator(1, 2)
