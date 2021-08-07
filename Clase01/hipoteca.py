saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    mes += 1
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
        total_pagado += pago_mensual + pago_extra 
        
    
    else:
        if saldo < pago_mensual:
            total_pagado += saldo * (1+tasa/12)
            saldo = saldo - saldo
            

        else:    
            saldo = saldo * (1+tasa/12) - pago_mensual 
            total_pagado += pago_mensual
            
    print(mes, round(total_pagado,2), round(saldo,2))        
        
    
              
      
print(f'Total pagado: {round(total_pagado, 2)} \nMeses: {mes}')