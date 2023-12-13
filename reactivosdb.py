# nuevo diccionario
# polvo muy volatil
import json

reactivos = {
    "15-101":{
        "nombre_quimico": "Resina Epoxica",
        
        "descripcion": "Liquido incoloro; viscosidad Media; libre de particulas",
        "peligro":"m",
        "indicacion":"",
        "revision":"",
        
        "viscosidad":"xxxcp"
        },
    "15-113":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "liquido poco viscoso blanco con olor a pintura acrilica",
        "peligro":"",
        "indicacion":"",
        "revision":"",
        
        "viscosidad":"200-500cp"
        },
    "15-132":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "liquido poco viscoso blanco con olor a pintura acrilica",
        "peligro":"",
        "indicacion":"",
        "revision":"",
        
        "viscosidad":"10-100cp"
        },
    "15-146":{
        "nombre_quimico": "BECKOPOX EP 386w/52WA Liquid coating resin",
        
        "descripcion": "Resina epoxidica soluble en agua",
        "peligro":"",
        "indicacion":"",
        "revision":"",
        
        "viscosidad":"300-1500cp"
        },
    "15-147":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "liquido bastante viscoso amarillo",
        "peligro":"",
        "indicacion":"",
        "revision":"",
        
        "viscosidad":"12000-21000cp"
        },
    "15-211":{
        "nombre_quimico": "EPODYL XY 678",
        
        "descripcion": "Liquido incoloro; viscosidad Media; libre de particulas",
        "peligro":"am",
        "indicacion":"",
        "revision":"",
        
        "viscosidad":""
        },
    "15-214":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Media; libre de particulas",
        "peligro":"am",
        "indicacion":"",
        "revision":"",
        
        "viscosidad":""
        },
    "15-222":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Media; libre de particulas",
        "peligro":"am",
        "indicacion":"",
        "revision":"",
        
        "viscosidad":"12000-21000cp"
        },
    "15-310":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Baja; libre de particulas",
        "peligro":"c",
        "indicacion":"Pese el 15-310 y añadalo a reactor por la escotilla del mismo, manteniedo el nitrogeno y la temperatura",
        "revision":"verifique que el liquido este libre de particulas",
        
        "viscosidad":""
        },
    "15-323":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Baja; libre de particulas",
        "peligro":"am",
        "indicacion":"Pese el 15-323 y con polipasto/plataforma añadalo a la tina/tambo",
        "revision":"verifique que el liquido este libre de particulas",
        
        "viscosidad":""
        },
    "15-332":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro o amarillo; viscosidad Media; libre de particulas",
        "peligro":"a",
        "indicacion":"Pese el 15-332 y y adicione al reactor",
        "revision":"verifique que el liquido este libre de particulas y sea claro",
        
        "viscosidad":""
        },
    "15-335":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Media; libre de particulas",
        "peligro":"tic",
        "indicacion":"Pese el 15-335 y con polipasto/plataforma añadalo al reactor",
        "revision":"verifique que el liquido este libre de particulas ",
        
        "viscosidad":""
        },
    "15-340-1":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Baja; libre de particulas",
        "peligro":"m",
        "indicacion":"Pese el 15-340-1 y con polipasto/plataforma añadalo a la tina/tambo",
        "revision":"verifique que el liquido este libre de particulas",
        
        "viscosidad":""
        },
    "15-342":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Baja; libre de particulas",
        "peligro":"c",
        "indicacion":"Pese el 15-342 y con polipasto/plataforma añadalo a la tina/tambo",
        "revision":"verifique que el liquido este libre de particulas",
        
        "viscosidad":""
        },
    "15-351":{
        "nombre_quimico": "Tolueno diisocianato",
        
        "descripcion": "Liquido ligeramente amarillo; viscosidad Baja; libre de particulas",
        "peligro":"ar",
        "indicacion":"De la cantidad de este reactivo, dividalo en diez partes, y agregue cada decima parte en intervalos de 5 minutos usando una cubeta limpia y seca",
        "revision":"verifique que el liquido este libre de particulas, y transparente.",
        
        "viscosidad":""
        },
    "15-415":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro o amarillo; viscosidad Media; libre de particulas",
        "peligro":"a",
        "indicacion":"Pese el 15-443 y y adicione al reactor. Caliente el reactor a 48±2°C para poder iniciar la reacción",
        "revision":"verifique que el liquido este fundido y tenga un color claro. Notifique al SPR si no es asi",
        
        "viscosidad":""
        },
    "15-416":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Baja; libre de particulas",
        "peligro":"",
        "indicacion":"Pese el 15-416 y añadalo al reactor, Cierre el reactor y suba la temperatura hasta 76°C±2°C",
        "revision":"",
        
        "viscosidad":""
        },
    "15-428-1":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Polvo amarillento",
        "peligro":"ia",
        "indicacion":"Pese el 15-428-1 y adicione bajo agitacion",
        "revision":"verifique que el polvo venga en pequeños granulos, caso contrario, triture antes de adicionar",
        
        "viscosidad":""
        },
    "15-429":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "liquido muy viscoso trasnparente sin olor",
        "peligro":"",
        "indicacion":"",
        "revision":"",
        
        "viscosidad":""
        },
    "15-443":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro o amarillo; viscosidad Media; libre de particulas",
        "peligro":"a",
        "indicacion":"Pese el 15-443 y y adicione al reactor",
        "revision":"verifique que el liquido este libre de particulas y sea totalmente claro",
        
        "viscosidad":""
        },
    "15-452-1":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Polvo amarillento",
        "peligro":"0",
        "indicacion":"Pese el 15-452-1 y agite a 600-750 r.p.m.",
        "revision":"verifique que el polvo tenga un color uniforme, sin grumos ni este apelmazado",
        
        "viscosidad":""
        },
    "15-470":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Media; libre de particulas",
        "peligro":"",
        "indicacion":"Pese el 15-470 y con polipasto/plataforma añadalo al reactor",
        "revision":"verifique que el liquido este libre de particulas y sea totalmente claro",
        
        "viscosidad":""
        },
    "15-494":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Polvo blanco de baja densidad",
        "peligro":"0",
        "indicacion":"Pese el 15-494, con plataforma añadalo a la tina/tambo",
        "revision":"Particulas solidas blancas de bajas densidad",
        
        "viscosidad":""
        },
    "15-495":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Polvo blanco de baja densidad",
        "peligro":"0",
        "indicacion":"Pese el 15-495, con plataforma añadalo a la tina/tambo",
        "revision":"Particulas solidas blancas de bajas densidad",
        
        "viscosidad":""
        },
    "15-499-3":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido marron verdoso poco viscoso",
        "peligro":"a",
        "indicacion":"Pese el 15-499-3 y con polipasto/plataforma añadalo a la tina/tambo",
        "revision":"verifique que el liquido este libre de particulas",
        
        "viscosidad":""
        },
    "15-501":{
        "nombre_quimico": "ALUMINIO ATOMIZADO",
        
        "descripcion": "polvo blanco ligero",
        "peligro":"",
        "indicacion":"",
        "revision":"",
        
        "viscosidad":""
        },
    "15-505":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "polvo blanco ligero",
        "peligro":"",
        "indicacion":"",
        "revision":"",
        
        "viscosidad":""
        },
    "15-515":{
        "nombre_quimico": "xxxxx",
    
        "descripcion": "Polvo blanco muy ligero",
        "peligro":"t",
        "indicacion":"Pese el 15-515, divida en 4 partes",
        "revision":"",
        
        "viscosidad":""
        },
    "15-537":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Polvo blanco ligero",
        "peligro":"t",
        "indicacion":"Pese el 15-537 y adicione bajo agitacion",
        "revision":"verifique que el polvo tenga un color uniforme, sin grumos ni este apelmazado",
        
        "viscosidad":""
        },
    "15-562":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Polvo Blanco",
        "peligro":"t",
        "indicacion":"Pese el 15-562 y adicione bajo agitacion, agitar durante 10-12 minutos y recircule 2 cubetas",
        "revision":"verifique que el polvo tenga un color uniforme, sin grumos ni este apelmazado",
        
        "viscosidad":""
        },
    "15-569":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "polvo ligero color hueso , un poco humedo",
        "peligro":"",
        "indicacion":"",
        "revision":"",
        
        "viscosidad":""
        },
    "15-520":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "polvo ligero blanco , un poco humedo",
        "peligro":"",
        "indicacion":"",
        "revision":"",
    
        "viscosidad":"xxxcp"
        },
    "15-580":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "polvo blanco de consistencia harinosa, un poco humedo",
        "peligro":"",
        "indicacion":"",
        "revision":"",
        
        "viscosidad":"xxxcp"
        },
    "15-581":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "polvo color hueso ligero",
        "peligro":"",
        "indicacion":"",
        "revision":"",
        
        "viscosidad":"xxxcp"
        },
    "15-600":{
        "nombre_quimico": "",
        "descripcion": "Liquido incoloro; viscosidad Media; libre de particulas",
        "peligro":"iat",
        "indicacion":"Pese el 15-607 y adicione a su tina/tambo",
        "revision":"verifique que el liquido este libre de particulas PELIGRO: NO GOLPEAR/AZOTAR RIESGO DE INCENDIO",
        "viscosidad":"xxx cp"
        },
    "15-602":{
        "nombre_quimico": "",
        "descripcion": "Liquido incoloro; viscosidad Baja; libre de particulas",
        "peligro":"iat",
        "indicacion":"Pese el 15-607 y adicione a su tina/tambo",
        "revision":"verifique que el liquido este libre de particulas PELIGRO: NO GOLPEAR/AZOTAR RIESGO DE INCENDIO",
        "viscosidad":"xxx cp"
        },
    "15-607":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Baja; libre de particulas",
        "peligro":"iat",
        "indicacion":"Pese el 15-607 y adicione a su tina/tambo",
        "revision":"verifique que el liquido este libre de particulas PELIGRO: NO GOLPEAR/AZOTAR RIESGO DE INCENDIO",
        
        "viscosidad":"xxxcp"
        },
    "15-610":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Baja; libre de particulas",
        "peligro":"ia",
        "indicacion":"Pese el 15-610, agite de 5 a 7 minutos y recircule",
        "revision":"verifique que el liquido este libre de particulas",
        
        "viscosidad":"xxxcp"
        },
    "15-612":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Baja; libre de particulas",
        "peligro":"ita",
        "indicacion":"Pese el 15-612 y con plataforma añadalo a la tina/tambo",
        "revision":"verifique que el liquido este libre de particulas PELIGRO: NO GOLPEAR/AZOTAR RIESGO DE INCENDIO",
        
        "viscosidad":"xxxcp"
        },
    "15-627":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Baja; libre de particulas",
        "peligro":"ia",
        "indicacion":"Pese el 15-627 y con polipasto/plataforma añadalo a la tina/tambo",
        "revision":"verifique que el liquido este libre de particulas",
        
        "viscosidad":"350-550cp"
        },
    "15-650":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Media; libre de particulas",
        "peligro":"cai",
        "indicacion":"Pese el 15-651-1 y bajo agitacion, adicione, deje mezclando durante 3-5 minutos",
        "revision":"",
        
        "viscosidad":"xxx cp"
        },
    "15-665":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Baja; libre de particulas",
        "peligro":"0",
        "indicacion":"Pese el 15-665 y con polipasto/plataforma añadalo a la tina/tambo",
        "revision":"verifique que el liquido este libre de particulas",
        
        "viscosidad":"xxx cp"
        },
    "15-669":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Baja; libre de particulas",
        "peligro":"m",
        "indicacion":"Pese el 15-340-1 y con polipasto/plataforma añadalo a la tina/tambo",
        "revision":"verifique que el liquido este libre de particulas",
        
        "viscosidad":"xxx cp"
        },
    "15-683":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Media; libre de particulas",
        "peligro":"0",
        "indicacion":"",
        "revision":"",
        
        "viscosidad":"xxx cp"
        },
    "15-690":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Baja; libre de particulas",
        "peligro":"iat",
        "indicacion":"Pese el 15-690 y plataforma añadalo a la tina/tambo",
        "revision":"verifique que el liquido este libre de particulas",
        
        "viscosidad":"xxx cp"
        },
    "15-690-1":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "liquido bastante viscoso amarillo",
        "peligro":"",
        "indicacion":"",
        "revision":"",
        
        "viscosidad":"xxx cp"
        },
    "15-692":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Dispersion azul; viscosidad Media; libre de particulas",
        "peligro":"ai",
        "indicacion":"",
        "revision":"",
        
        "viscosidad":"xxxcp"
        },
    "15-698-1":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Media; libre de particulas",
        "peligro":"0",
        "indicacion":"",
        "revision":"",
        
        "viscosidad":"xxxcp"
        },
    "15-699-2":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Media; libre de particulas",
        "peligro":"0",
        "indicacion":"",
        "revision":"",
        
        "viscosidad":"xxxcp"
        },
    "15-699-8":{
        "nombre_quimico": "Etanol",
        
        "descripcion": "Liquido incoloro de olor caracteristico, sabor quemante",
        "peligro":"0",
        "indicacion":"",
        "revision":"",
        
        "viscosidad":"xxxcp"
        },
    "15-702":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Media; libre de particulas",
        "peligro":"0",
        "indicacion":"",
        "revision":"",
        
        "viscosidad":"xxxcp"
        },
    "25-501":{
        "nombre_quimico": "xxxxx",
        
        "descripcion": "Liquido incoloro; viscosidad Baja; libre de particulas",
        "peligro":"ai",
        "indicacion":"Quince minutos antes de terminar el cocinado, pese el 15-501, y adicione al reactor por vacio a 50cm Hg",
        "revision":"verifique que el liquido este libre de particulas",
        
        "viscosidad":"xxxcp"
        }
    }
# GUARDAMOS  LA DATA EN UN ARCHIVO .JSON

with open('reactivos.json', 'w') as archivo:
    json.dump(reactivos,archivo)
