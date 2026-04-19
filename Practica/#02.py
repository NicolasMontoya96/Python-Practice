
def pagar_deuda(monto_inicial, abono_mensual):
    deuda = monto_inicial
    pago_mensual = abono_mensual
    tasa_interes = 0.02 # 2%
    mes = 1
    total_pagado = 0
    
    # 1. Validación previa: calculamos el primer interés para comparar
    interes_inicial = deuda * tasa_interes

    if abono_mensual < interes_inicial:
        print("Debe realizar un pago igual o superior al interes generado")
    else:
        # 2. El bucle ahora es "hijo" del else (está indentado)
        while deuda > 0:
            # 3. Recalculamos el interés CADA mes sobre la deuda actual
            interes_mensual = deuda * tasa_interes
            deuda += interes_mensual      

            if deuda >= pago_mensual:
                total_pagado += pago_mensual
                deuda -= pago_mensual
            else:
                total_pagado += deuda
                deuda -= deuda
            
            print(f"Mes {mes}: Pago realizado, te quedan {deuda:,.0f}")
            mes += 1
            return mes - 1
        
        # Este print también es parte del else, se muestra al terminar el pago
        print(f"El total pagado es de {total_pagado:,.0f}")

# Captura de datos fuera de la función
valor_deuda = float(input("Cuánto debes actualmente? "))
abono_usuario = float(input("Cuánto quieres abonar? "))

# Llamada a la función
pagar_deuda(valor_deuda, abono_usuario)
