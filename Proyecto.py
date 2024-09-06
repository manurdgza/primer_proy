def precio_bajo(precio_menor):
    precio_1=int(input("Cual fue el precio de la mensualidad pasada?"))
    precio_2=int(input("Cual fue el precio de la mensualidad de este mes?"))
    if precio_1>precio_2:
        return ("El precio fue mas bajo por", precio_menor)

def precio_alto(precio_mayor):
    precio_1=int(input("Cual fue el precio de la mensualidad pasada?"))
    precio_2=int(input("Cual fue el precio de la mensualidad de este mes?"))
    if precio_1<precio_2:
        return ("Este recibo fue mas alto que el mes pasado, deberias poner mas atencion al consumo del agua en casa", precio_mayor)

def faltante_meta(diferencia_meta):
    precio_1=int(input("Cual fue el precio de su ultimo recibo del agua?"))
    diferencia_meta=int(input("Cual es su meta de precio para el agua?"))
    return ("Vas por buen camino, intenta reducir tiempos al bañar o al lavar platos y lo lograras", meta)
    
def precio_dia(precio_diario):
    precio=int(input("Cual fue el precio de su recibo?"))
    dias=int(input("Cuantos días duro este mes?"))
    return ("Su total diario fue de $",precio_diario)

def precio_año(precio_anual):
    precio=int(input("Cual fue el precio de su recibo?"))
    dias=int(input("Cuantos dias duro este mes?"))
    precio_anual=(precio_diario*dias)
    return ("Si sigue asi su gasto anual de agua sera de $","%.2f"%(precio_anual))

def meta_año(meta_anual):
    meta_anual=int(input("Le gustaria calcular cuanto ocuparia gastar al dia para llegar a una meta anual?"))
    calculo_anual=(meta/365)
    return ("Su consumo diario deberia de ser de $","%.2f"%(calculo_anual))

def litros(consumo_agua):
    precio=int(input("Cual fue el precio de su recibo?"))
    consumo_agua=(precio/0.03)
    return ("Sus litros utilizados este mes fueron","%.2f"%consumo_agua, "litros")

def litros_persona(consumo_persona):
    precio=int(input("Cual fue el precio de su recibo?"))
    personas=int(input("Cuantas personas son en su casa?"))
    consumo_persona=(consumo_agua/personas)
    return ("El consumo por persona en su casa es de " "%.2f"%(consumo_persona), "litros")

print("Hola, este software te va a ayudar a rastrear tu consumo de agua")
print("Campanario(1)\nEl refugio(2)\nAlamos(3)\nJuriquilla(4)\nJurica(5)\nCentro(6)\nEl Pueblito(7)")
opcion_qro=int(input("En que parte de Queretaro vives, introduce el numero junto a la opcion"))
if(opcion_qro==1):
    print("hola")
#suma1 a campanario
elif(opcion_qro==2):
    print("hola")
#suma 1 a el refugio
elif(opcion_qro==3):
    print("hola")
#suma 1 a alamos
elif(opcion_qro==4):
    print("hola")
#suma 1 a juriquilla
elif(opcion_qro==5):
    print("hola")
#suma 1 a jurica
elif(opcion_qro==6):
    print("hola")
#suma 1 a el centro
elif(opcion_qro==7):
    print("hola")
#suma 1 a el pueblito

#Aqui va a ir un contador de cuando seleccionen en que parte viven poder hacer un conteo acerca de cuanta agua consume cada parte de Qro
print("Comparar precios del agua del mes actual y el ultimo(1)\nPoner una meta acerca del uso del agua(2)"
"\nCalcular su consumo diario(3)\nCalcular cuantos litros uso este mes(4)")
opcion_agua=int(input("Que opcion quieres realizar?"))
if(opcion_agua==1):
    precio_1=int(input("Cual fue el precio de tu recibo de ultimo mes del agua?"))
    precio_2=int(input("Cual fue el precio de tu recibo atual de agua?"))
    if(precio_1>precio_2):
        precio_menor=(precio_1-precio_2)
        print("Felicidades, ahorrando agua bajaste tu consumo por $",precio_menor )
    elif(precio_1<precio_2):
        precio_mayor=precio_2-precio_1
        print("Este recibo fue mas alto que el mes pasado, deberias poner mas atencion al consumo del agua en casa por $", precio_mayor)
    elif(precio_1==precio_2):
        print("Su consumo de agua fue el mismo que el mes pasado, nada mal, pero deberia intentar bajar ese precio")
elif(opcion_agua==2):
    precio_1=int(input("Cual fue el precio de su ultimo recibo del agua?"))
    meta=int(input("Cual es su meta de precio para el agua?"))
    diferencia_meta=(precio_1-meta)
    if(diferencia_meta<50):
        print("Vas por buen camino, intenta reducir tiempos al bañar o al lavar platos y lo lograras, solo te falta $", diferencia_meta)
    elif(diferencia_meta>50):
        print("Aún estas un poco lejos de la meta, deberias esforzarte más al ahorrar agua, te falta $",diferencia_meta )
elif(opcion_agua==3):
    precio=int(input("Cual fue el precio de su recibo?"))
    dias=int(input("Cuantos días duro este mes?"))
    precio_diario=(precio/dias)
    print("Su precio diario fue de $""%.2f"%(precio_diario))
    precio_anual=(precio_diario*365)
    print("Si sigue asi su gasto anual de agua sera de $","%.2f"%(precio_anual))
    print("Si gusta calcular una meta anual seleccione(1), de lo contrario(2)")
    meta_anual=int(input("Le gustaria calcular cuanto ocuparia gastar al dia para llegar a una meta anual?"))
    if(meta_anual==1):
        meta=int(input("Cuanto le gustaria gastar al año en agua?"))
        calculo_anual=(meta/365)
        print("Su consumo diario deberia de ser de $","%.2f"%(calculo_anual))
elif(opcion_agua==4):
    precio=int(input("Cual fue el precio de su recibo?"))
    consumo_agua=(precio/0.03)
    print("Sus litros utilizados este mes fueron","%.2f"%consumo_agua, "litros")
    print("El promedio por persona utilizado mensualmente es de 6000 litros")
    personas=int(input("Cuantas personas son en su casa?"))
    consumo_persona=(consumo_agua/personas)
    print("El consumo por persona en su casa es de " "%.2f"%(consumo_persona), "litros")




    
    



    
        
        
        

    
