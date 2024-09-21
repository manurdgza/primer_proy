def precio_bajo(a,b): #YA SIRVE 
    if precio_1>precio_2:
        return ("Felicidades!! El precio fue mas bajo por", precio_menor)
    if precio_1==precio_2:
        return("Su consumo de agua fue el mismo que el mes pasado, nada mal, pero deberia intentar bajar ese precio")
    return("Este recibo fue mas alto que el mes pasado, deberias poner mas atencion al consumo del agua en casa por $", precio_mayor)
    

def faltante_meta(a,b): #YA SIRVE
    diferencia_meta=(a-b)
    if diferencia_meta<50:
        return ('Vas por buen camino, intenta reducir tiempos al bañar o al lavar platos y lo lograras, te falta $',diferencia_meta,'para lograrlo')
    return ("Aún estas un poco lejos de la meta, deberias esforzarte más al ahorrar agua, te falta $",diferencia_meta )
    
def precio_dia(a,b):
    precio_diario=(a/b)
    return ("Su total diario fue de $",precio_diario) #YA SIRVE

def precio_año(a,b):
    precio_anual=(precio_diario*365)
    return ("Si sigue asi su gasto anual de agua sera de $","%.2f"%(precio_anual)) #YA SIRVE

def meta_año(meta_anual):
    calculo_anual=(meta/365)
    return ("Su consumo diario deberia de ser de $","%.2f"%(calculo_anual)) #YA SIRVE

def litros(consumo_agua):
    l=0.03
    consumo_agua=(precio/l)
    return ("Sus litros utilizados este mes fueron","%.2f"%consumo_agua, "litros") #YA SIRVE

def litros_persona(consumo_agua,personas):
    consumo_agua=int(input())
    personas=int(input())
    consumo_persona=(consumo_agua//personas)
    return ("El consumo por persona en su casa es de " "%.2f"%(consumo_persona)) #YA SIRVE

campanario=0
el_refugio=0
alamos=0
juriquilla=0
jurica=0
el_centro=0
el_pueblito=0
def lugar_qro(a): 
    if opcion==1:
        campanario=campanario+1
        return(campanario)
    if opcion==2:
        el_refugio=el_refugio+1
        return(el_refugio)
    if opcion==3:
        alamos=alamos+1
        return(alamos)
    if opcion==4:
        juriquilla=juriquilla+1
        return(juriquilla)
    if opcion==5:
        jurica=jurica+1
        return(jurica)
    if opcion==6:
        el_centro=el_centro+1
        return(el_centro)
    if opcion==7:
        el_pueblito=el_pueblito+1
        return(el_pueblito)
        

print("Hola, este software te va a ayudar a rastrear tu consumo de agua")
#print("Campanario(1)\nEl refugio(2)\nAlamos(3)\nJuriquilla(4)\nJurica(5)\nCentro(6)\nEl Pueblito(7)")
lista_lugar=["Campanario(1)","El refugio(2)","Alamos(3)","Juriquilla(4)","Jurica(5)","El centro(6)","El pueblito(7)"]
for lugar in lista_lugar:
    print(lugar)
opcion_qro=int(input("En que parte de Queretaro vives, introduce el numero junto a la opcion"))
if(opcion_qro==1):
    contador=0
    contador=contador+1
    if contador==1:
        print("Es la primera persona de este lugar que usa el programa")
    else:
        print("Van",contador,"personas que usan este programa de ese lugar")
if (opcion_qro==2):
    contador=0
    contador=contador+1
    if contador==1:
        print("Es la primera persona de este lugar que usa el programa")
    else:
        print("Van",contador,"personas que usan este programa de ese lugar")
elif(opcion_qro==3):
    contador=0
    contador=contador+1
    if contador==1:
        print("Es la primera persona de este lugar que usa el programa")
    else:
        print("Van",contador,"personas que usan este programa de ese lugar")
elif(opcion_qro==4):
    contador=0
    contador=contador+1
    if contador==1:
        print("Es la primera persona de este lugar que usa el programa")
    else:
        print("Van",contador,"personas que usan este programa de ese lugar")
elif(opcion_qro==5):
    contador=0
    contador=contador+1
    if contador==1:
        print("Es la primera persona de este lugar que usa el programa")
    else:
        print("Van",contador,"personas que usan este programa de ese lugar")
elif(opcion_qro==6):
    contador=0
    contador=contador+1
    if contador==1:
        print("Es la primera persona de este lugar que usa el programa")
    else:
        print("Van",contador,"personas que usan este programa de ese lugar")
elif(opcion_qro==7):
    contador=0
    contador=contador+1
    if contador==1:
        print("Es la primera persona de este lugar que usa el programa")
    else:
        print("Van",contador,"personas que usan este programa de ese lugar")

#Aqui va a ir un contador de cuando seleccionen en que parte viven poder hacer un conteo acerca de cuanta agua consume cada parte de Qro
#print("Comparar precios del agua del mes actual y el ultimo(1)\nPoner una meta acerca del uso del agua(2)"
#"\nCalcular su consumo diario(3)\nCalcular cuantos litros uso este mes(4)")
lista_opcion=["Comparar precios del agua del mes atual y mes pasado(1)","Poner meta del uso del agua(2)","Calcular su consumo diario(3)","Calcular litros usados este mes(4)"]
for opcion in lista_opcion:
    print(opcion)
opcion_agua=int(input("Que opcion quieres realizar?"))
if opcion_agua>4:
    print ("Esta no es una opción valida")
if(opcion_agua==1):
    precio_1=int(input("Cual fue el precio de tu recibo de ultimo mes del agua?"))
    precio_2=int(input("Cual fue el precio de tu recibo actual de agua?"))
    if(precio_1>precio_2):
        precio_menor=(precio_1-precio_2)
        print(precio_bajo(precio_1,precio_2))
    elif(precio_1<precio_2):
        precio_mayor=precio_2-precio_1
        print (precio_bajo(precio_1,precio_2))
    elif(precio_1==precio_2):
        print (precio_bajo(precio_1,precio_2))
elif(opcion_agua==2):
    precio_1=int(input("Cual fue el precio de su ultimo recibo del agua?"))
    meta=int(input("Cual es su meta de precio para el agua?"))
    diferencia_meta=(precio_1-meta)
    if(diferencia_meta<50):
        print (faltante_meta(precio_1,meta))
    elif(diferencia_meta>50):
        print (faltante_meta(precio_1,meta))
elif(opcion_agua==3): #YA MANDA LLAMAR FUNCION
    precio=int(input("Cual fue el precio de su recibo?"))
    dias=int(input("Cuantos días duro este mes?"))
    precio_diario=(precio/dias)
    print(precio_dia(precio,dias))
    precio_anual=(precio_diario*365)
    print (precio_año(precio_anual,365))
    print("Si gusta calcular una meta anual seleccione(1), de lo contrario(2)")
    meta_anual=int(input("Le gustaria calcular cuanto ocuparia gastar al dia para llegar a una meta anual?"))
    if(meta_anual==1):
        meta=int(input("Cuanto le gustaria gastar al año en agua?"))
        calculo_anual=(meta/365)
        print("Su consumo diario deberia de ser de $","%.2f"%(calculo_anual))
elif(opcion_agua==4): #YA MANDA LLAMAR FUNCION
    precio=int(input("Cual fue el precio de su recibo?"))
    consumo_agua=(litros(precio))
    print(consumo_agua)
    print("El promedio por persona utilizado mensualmente es de 6000 litros")
    personas=int(input("Cuantas personas son en su casa?"))
    consumo_personal=(litros_persona(consumo_agua,personas))
    print (consumo_personal)




    
    



    
        
        
        

    
