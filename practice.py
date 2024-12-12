def calcular_precio(peso):
    precio_producto= 100
    
    if peso <= 5  :
        descuento=0.05
    elif peso <= 10 :
        descuento= 0.1
    else:
        descuento=0.2

    descuento_aplicado= precio_producto * descuento
    precio_final= precio_producto - descuento_aplicado

    return precio_final

prueba = calcular_precio(11)
print(prueba)

