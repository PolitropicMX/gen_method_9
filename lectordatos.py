import json
from just_the_module import Save_module
with open('datos.json', 'r') as archivo:
    datos_cargados = json.load(archivo)
##print(datos_cargados)

for i,j in enumerate(datos_cargados):
    print(j)
    for k in datos_cargados[str(j)].keys():
        print(f'(1) {k}')
        for g in datos_cargados[str(j)][str(k)]:
            print(f'(2) {g}')
##
##chuck_diccionario = {
##            "Bullton 2013":{ # 25-105
##            "Banner 1":"b2", # BANNER DE  EQUIPO DE PROTECCION
##            "Banner 2":"b8", # MANTENER TU REACTOR LIMPIO
##            "Banner 3":"b7", # BANNER DE CONSIDERACIONES ANTES DE USAR E PROCESO
##            "Paso 1":{
##                "texto":"Paso 1) Fundición del 15-415: Se deja por 12 horas el tambo del 15-415 a una temperatura de 105±5°C, se saca del horno, se abre uno de los tapones para liberar presión"
##                },
##            "Paso 2":{
##                "texto":"Paso 2) Adicion del 15-415 al reactor: se pesa y se carga al reactor por medio de uso del vacio la cantidad de 15-415 requerida segun la Orden de Producción"
##                },
##            "15-415":{
##                "descripcion": "Sólido/Liquido Fundido incoloro o amarillo; viscosidad Alta-Media; libre de particulas",
##                "peligro":"a",
##                "indicacion":"Cuidado!: Tambor Caliente, Pese el tambor lleno y succione el peso necesario para la fabricacion del producto",
##                "revision":"verifique que el liquido este fundido y tenga un color claro. Notifique al SPR si no es asi"
##                },
##            "Paso 3":{
##                "texto":"Paso 3) Deshidratacion del 15-415: Una vez el 15-415 de forma liquida en el reactor, se cierra, se calienta a 110-115°C y con agitación, se aplica un vacio de 30-60 cmHg durante 30 minutos"
##                },
##            "Paso 4":{
##                "texto":"Paso 4) Nitrogeno en los tambores: Mientras se lleva a cabo la deshidratación, coloque una capa de Nitrogeno en/los tambores de 15-415, para su posterior uso"
##                },
##            "Paso 5":{
##                "texto":"Consejo) Para verificar el color claro de sus materias primas, utilice cubetas blancas, las cuales deben estar perfectamente limpias y secas. Si usas envases extras, siempre deben estar perfectamente limpios y secos"
##                },
##            "Paso 6":{
##                "texto":"Paso 5) Enfriamiento del 15-415: Una vez terminada la deshidratación, se enfria el reactor con agua hasta llegar a una temperatura de 48±2°C"
##                },
##            "Paso 7":{
##                "texto":"Paso 6) Adiciones del 15-351: Una vez alcanzada la temperatura estable, pese la cantidad del 15-351, y haga adiciones cada 5 minutos en un tiempo total de entre 45 y 50 minutos. Cuide en este punto de que la temperatura marcada no exceda los 55°C. Recomendacion: a los 53°C agregue agua de enfriamiento"
##                },
##            "15-351":{
##                "descripcion": "Liquido ligeramente amarillo; viscosidad Baja",
##                "peligro":"ar",
##                "indicacion":"Haga adiciones de 15-351 y que no exceda la temperatura de 53±2°C",
##                "revision":"verifique que el liquido este libre de particulas, y transparente."
##                },
##            "Paso 8":{
##                "texto":"Paso 7) Cocinado: Una vez terminada la adición, espere 15 minutos a que estabilice, ahora la temperatura de la mezcla debe ser 83±2°C bajo agitación constante. Es importante que mantenga la temperatura a 83(+/-)2°C al realizar el cocinado para obtener un %NCO deseado: Duración del cocinado: 2 horas"
##                },
##            "Paso 9":{
##                "texto":"Paso 8) Adicion del 25-501: 15 minutos antes de terminar las 2 horas del cocinado, agregue lo indicado de 25-501 con vacío de 50 cmHG segun la Orden de Producción "
##                },
##            "25-501":{
##                "descripcion": "Liquido incoloro; viscosidad Baja; libre de particulas",
##                "peligro":"ai",
##                "indicacion":"Quince minutos antes de terminar el cocinado, pese el 25-501 y adicione al reactor",
##                "revision":""
##                },
##            "Paso 10":{
##                "texto":"El Bullton 2013 es un material muy sensible a la humedad, por lo que se recomienda al momento de envasar, poner una capa de nitrogeno sobre la superficie del prepolimero y cerrar perfectamente el envase."
##                },
##            "Paso 11":{
##                "texto":"La temperatura de envasado es de 60±2°C"
##                },
##            "Equipo a utilizar": {
##                "Equipo a utilizar":"REACTOR, POLIPASTO" 
##                },
##            "Envase":{
##                "Envase_producto":"TAMBOR NUEVO o EXCLUSIVAMENTE de 15-315, no usar ningun otro, solo los 2 anteriores" ,
##                "Envase_control":"Lata de 1/2"
##                # PARA ESTE PRODUCTO UNICAMENTE
##                # El bullton 5085 es un material muy sensible a la humedad por lo que se recomienda al momento de envasar, poner una capa de nitrogeno sobre la superficie del prepolimero y cerrar perfectamente el envase. La temperatura de envasado es de 60°C±2°C
##                }
##            }
##        }
##chuck_diccionario["producto2"] = datos_cargados["producto2"]3
##print(chuck_diccionario)
##
who = datos_cargados
for i,j in enumerate(who):
    print(j)
    for k in who[str(j)].keys():
        print(f'(1) {k}')
        for g in who[str(j)][str(k)]:
            print(f'(2) {g}')

##f = Save_module()
##f.active_module("Bullton 2013","24-102",chuck_diccionario)
