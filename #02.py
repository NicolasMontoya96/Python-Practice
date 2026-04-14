
def pagar_deuda():
    deuda = 1500000
    pago_mensual = 100000
    tasa_interes = 0.02 #2 %
    mes = 1
    total_pagado = 0
    while deuda > 0:
        interes_mensual = deuda * tasa_interes     #Saco el interes mensual a pagar
        deuda += interes_mensual      
                
        if deuda >= pago_mensual:
            total_pagado += pago_mensual
            deuda -= pago_mensual                      #Resto los 100 mil de la cuota a la deuda
            
        else:
            total_pagado += deuda
            deuda -= deuda
            

    
        print(f"Mes {mes}: Pago realizado, te quedan {deuda:,.0f}")
        mes += 1
        

        
    print(f"El total pagado es de {total_pagado:,.0f}")
    
    
pagar_deuda()
