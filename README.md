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
print("Comparar precios del agua del mes actual y el ultimo(1)\nPoner una meta acerca del uso del agua(2)\n\
Ver información acerca del agua en Queretaro(3)\n")
opcion_agua=int(input("Que opcion quieres realizar?"))
if(opcion_agua==1):
    precio_1=int(input("Cual fue el precio de tu recibo de ultimo mes del agua?"))
    precio_2=int(input("Cual fue el precio de tu recibo atual de agua?"))
    if(precio_1>precio_2):
         precio_menor=(precio_1-precio_2)
         print("Felicidades, ahorrando agua bajaste tu consumo por")
    elif(precio_1<precio_2):
             print("Este recibo fue mas alto que el mes pasado, deberias poner mas atencion al consumo del agua en casa")\
                         #PONER QUE TANTO DINERO FUE MAYOR AL MES PASADO EN LA LINEA 37
    elif(precio_1==precio_2):
        print("Su consumo de agua fue el mismo que el mes pasado, nada mal, pero deberia intentar bajar ese precio")
elif(opcion_agua==2):
    precio_1=int(input("Cual fue el precio de su ultimo recibo del agua?"))
    meta=int(input("Cual es su meta de precio para el agua?"))
    diferencia_meta=(precio_1-meta)
    if(diferencia_meta<50):
        print("Vas por buen camino, intenta reducir tiempos al bañar o al lavar platos y lo lograras")#PONER CUANTO FALTA PARA LLEGAR A LA META
    elif(diferencia_meta>50):
        print("Aún estas un poco lejos de la meta, deberias esforzarte más al ahorrar agua")#PONER CUANTO FALTA PARA LLEGAR A LA META
elif(opcion_agua==3):
