
def pagar_deuda():
    deuda = 1500000
    pago_mensual = 100000
    tasa_interes = 0.02 #2 %
    while deuda > 0:
        interes_mensual = deuda * tasa_interes     #Saco el interes mensual a pagar
        deuda += interes_mensual
        if deuda >= pago_mensual:

            deuda -= pago_mensual                      #Resto los 100 mil de la cuota a la deuda
        else:
            deuda -= deuda
            print(f"Pago realizado, te quedan {deuda}")
            break
        
        print(f"Pago realizado, te quedan {deuda}")
        

pagar_deuda()