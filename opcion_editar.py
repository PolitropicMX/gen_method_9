import tkinter as tk
from tkinter import ttk
##from productos_reactivos import Productos
from tkinter import messagebox
import json
from just_the_module import Save_module

def mostrar_lista(diccionario):
            # SE CREA UN ARRAY VACIO
        treeview_data = []
            # UN CONTADOR QUE CUENTA CADA ELEMENTO
        counter = 0
            # POR CADA PRODUCTO EN PRODUCTOS
        for i,producto in enumerate(diccionario):
                # SE CONTABILIZA CADA PRODUCTO
            counter += 1
                # AQUI SE AÑADE 
            treeview_data.append(("","end",counter,producto,("a","b")))
                # SE GUARDA EL NUMERO DE CONTEO
            childof = counter
            for k,data in enumerate(diccionario[producto]):
                counter += 1
                treeview_data.append((childof,"end",counter,data,("a","b")))
        return treeview_data

def editar(root): # AQUI INICIA EDICION DE UN METODO
    with open('datos.json', 'r') as archivo:# extraer la info previa
            datos_cargados = json.load(archivo)# antigua info
    combo_productos_var = tk.StringVar()
    dict_producto = {}
    def on_enter(event):
        event.widget.invoke()
    def save_method():
        nonlocal dict_producto
        print(dict_producto)
        nombre_producto = name_prod_entry.get()
        with open('datos.json', 'r') as archivo:# extraer la info previa
            datos_cargados = json.load(archivo)# antigua info
        datos_cargados[nombre_producto] = dict_producto[nombre_producto]
        # Se deben guardar los cambios de los entry's
        nombre = name_prod_entry.get()
        noinv = no_prod_entry.get()
        picto = picto_prod_entry.get()
        envprod = etiq_prod_entry.get()
        envmues = mues_prod_entry.get()
        equipo = equi_labe_entry.get()
        malla = mall_labe_entry.get()
##        print()
        print(f" envase del producto es: {envprod} para control es: {envmues}")
        datos_cargados[nombre_producto]["Informacion"]["no inv"] = noinv
        datos_cargados[nombre_producto]["Informacion"]["pictogramas"] = picto
        if malla == "":
                datos_cargados[nombre_producto]["Envase"] =  {"malla":"no"}
        else:
                datos_cargados[nombre_producto]["Envase"] =  {"malla":f"{malla}"}
        datos_cargados[nombre_producto]["Envase"]["Envase_producto"] = envprod
        datos_cargados[nombre_producto]["Envase"]["Envase_control"] = envmues
        datos_cargados[nombre_producto]["Equipo a utilizar"]["Equipo a utilizar"] = equipo
        print(f"Los datos guardados quedan como: \n{datos_cargados[nombre_producto]}")
        with open('datos.json', 'w') as archivo:
            json.dump(datos_cargados,archivo)  
        third_window.destroy()
    def option_selected(event): # ESTA FUNCION ES PARA EL COMBOBOX: REACTIVO, PASO, BANNER
        nonlocal datos_cargados, dict_producto
        selected_option = combo_productos_var.get()
        counter = 0
        treeview_data = []
        dict_producto = {selected_option : datos_cargados[selected_option]}
        # ELIMINAMOS LA INFORMACION EN LOS CAMPOS
        name_prod_entry.delete(0,tk.END)
        no_prod_entry.delete(0,tk.END)
        picto_prod_entry.delete(0,tk.END)
        etiq_prod_entry.delete(0,tk.END)
        mues_prod_entry.delete(0,tk.END)
        equi_labe_entry.delete(0,tk.END)
        mall_labe_entry.delete(0,tk.END)
            # POR CADA PRODUCTO EN PRODUCTOS
        if selected_option in (datos_cargados):
                # SE CONTABILIZA CADA PRODUCTO
            counter += 1
                # AQUI SE AÑADE 
            treeview_data.append(("","end",counter,selected_option,("a","b")))
                # SE GUARDA EL NUMERO DE CONTEO
            childof = counter
            name_prod_entry.insert(0,selected_option)
            for k,data in enumerate(datos_cargados[selected_option]):
                counter += 1
                treeview_data.append((childof,"end",counter,data,("a","b")))
                if data == "Informacion":
                    no_prod_entry.insert(0,datos_cargados[selected_option]["Informacion"]["no inv"])
                    picto_prod_entry.insert(0,datos_cargados[selected_option]["Informacion"]["pictogramas"])
                elif data == "Envase":
                    if "Envase_producto" in datos_cargados[selected_option]["Envase"]:
                        etiq_prod_entry.insert(0,datos_cargados[selected_option]["Envase"]["Envase_producto"])
                    if "Envase_control" in datos_cargados[selected_option]["Envase"]:
                        mues_prod_entry.insert(0,datos_cargados[selected_option]["Envase"]["Envase_control"])
                    if "malla" in datos_cargados[selected_option]["Envase"]:
                        mall_labe_entry.insert(0,datos_cargados[selected_option]["Envase"]["malla"])
                elif data == "Equipo a utilizar":
                    equi_labe_entry.insert(0,datos_cargados[selected_option]["Equipo a utilizar"]["Equipo a utilizar"])
                
        treeview.delete(*treeview.get_children())
        for item in treeview_data:
            treeview.insert(parent=item[0], index=item[1], iid=item[2], text=item[3], values=item[4],open=True)
                    
    def editar_bloque():
        nonlocal datos_cargados, dict_producto
        def tipo_bloque(bloque):
            nombre_producto = name_prod_entry.get()
            if bloque[0] == "1" or bloque[0] == "2":# Es REACTIVO
                def save():
                    dict_producto[nombre_producto][bloque]["descripcion"] = name_reac_entry.get("1.0", "end-1c")
                    dict_producto[nombre_producto][bloque]["peligro"] = name_pict_entry.get("1.0", "end-1c")
                    dict_producto[nombre_producto][bloque]["indicacion"] = name_indi_entry.get("1.0", "end-1c")
                    dict_producto[nombre_producto][bloque]["revision"] = name_revi_entry.get("1.0", "end-1c")
                    edit_window.destroy()
                def cerrar():
                    edit_window.destroy()
                # Ventana
                edit_window = tk.Toplevel(third_window)
                edit_window.title(f"{bloque}")
                # FRAMES -----------------------------------------------------------------
                reactivo = tk.Frame(edit_window)
                reactivo.grid(row=0,column=0,padx=5,pady=5)
                campos = tk.Frame(edit_window)
                campos.grid(row=1,column=0,padx=5,pady=5)
                botones_edit = tk.Frame(edit_window)
                botones_edit.grid(row=2,column=0,padx=5,pady=5)
                name_label = ttk.Label(reactivo, text=f"Estas editando el REACTIVO ")
                name_label.grid(row=0,column=0,padx=5,pady=5)
                name_entry = ttk.Entry(reactivo,font=("Helvetica",15))
                name_entry.grid(row=0, column=1,padx=5,pady=5)
                name_entry.insert(0,bloque)
                #  ENTRYS -----------------------------------------------------------------
                # ETIQUETA
                name_reac = tk.Label(campos, text="Descripción", font=('Arial', 9))
                name_reac.grid(row=0, column=0,padx=5,pady=5)
                # ENTRY        
                name_reac_entry = tk.Text(campos,font=("Helvetica",10), width=20, height=10)
                name_reac_entry.grid(row=0, column=1,padx=5,pady=5)
                name_reac_entry.insert(tk.END,dict_producto[nombre_producto][bloque]["descripcion"])
                # ETIQUETA
                name_pict = tk.Label(campos, text="Peligro", font=('Arial', 9))
                name_pict.grid(row=1, column=0,padx=5,pady=5)
                # ENTRY        
                name_pict_entry = tk.Text(campos,font=("Helvetica",10), width=20, height=10)
                name_pict_entry.grid(row=1, column=1,padx=5,pady=5)
                name_pict_entry.insert(tk.END,dict_producto[nombre_producto][bloque]["peligro"])
                # ETIQUETA
                name_indi = tk.Label(campos, text="Indicación", font=('Arial', 9))
                name_indi.grid(row=0, column=3,padx=5,pady=5)
                # ENTRY        
                name_indi_entry = tk.Text(campos,font=("Helvetica",10), width=20, height=10)
                name_indi_entry.grid(row=0, column=2,padx=5,pady=5)
                name_indi_entry.insert(tk.END,dict_producto[nombre_producto][bloque]["indicacion"])
                # ETIQUETA
                name_revi = tk.Label(campos, text="Revision", font=('Arial', 9))
                name_revi.grid(row=1, column=3,padx=5,pady=5)
                # ENTRY        
                name_revi_entry = tk.Text(campos,font=("Helvetica",10), width=20, height=10)
                name_revi_entry.grid(row=1, column=2,padx=5,pady=5)
                name_revi_entry.insert(tk.END,dict_producto[nombre_producto][bloque]["revision"])
                # BUTTONS ----------------------------------------------------------------
                guardar = ttk.Button(botones_edit,text="Guardar",command=save).grid(row=0, column=0,padx=5,pady=5)
                cerrar =  ttk.Button(botones_edit,text="Cerrar",command=cerrar).grid(row=0, column=1,padx=5,pady=5)
            elif bloque[0] == "P": # Eligio Paso
                def save():
                    dict_producto[nombre_producto][bloque]["texto"] = name_reac_entry.get("1.0", "end-1c")
                    edit_window.destroy()
                def cerrar():
                    edit_window.destroy()
                # Ventana
                edit_window = tk.Toplevel(third_window)
                edit_window.title(f"{bloque}")
                # FRAMES -----------------------------------------------------------------
                reactivo = tk.Frame(edit_window)
                reactivo.grid(row=0,column=0,padx=5,pady=5)
                campos = tk.Frame(edit_window)
                campos.grid(row=1,column=0,padx=5,pady=5)
                botones_edit = tk.Frame(edit_window)
                botones_edit.grid(row=2,column=0,padx=5,pady=5)
                # ETIQUETA
                name_reac = tk.Label(campos, text=f"{bloque}", font=('Arial', 9))
                name_reac.grid(row=0, column=0,padx=5,pady=5)
                # ENTRY        
                name_reac_entry = tk.Text(campos,font=("Helvetica",10), width=30, height=10)
                name_reac_entry.grid(row=0, column=1,padx=5,pady=5)
                name_reac_entry.insert(tk.END,datos_cargados[nombre_producto][bloque]["texto"])
                # BUTTONS ----------------------------------------------------------------
                guardar = ttk.Button(botones_edit,text="Guardar",command = save).grid(row=0, column=0,padx=5,pady=5)
                cerrar =  ttk.Button(botones_edit,text="Cerrar",command=cerrar).grid(row=0, column=1,padx=5,pady=5)
            elif bloque[0].upper() == "B":
                def save():                    
                    selected_option = banners_var.get()
                    dict_producto[nombre_producto][bloque] = selected_option[0:2]
                    edit_window.destroy()
                def cerrar():
                    edit_window.destroy()
                # Ventana
                edit_window = tk.Toplevel(third_window)
                edit_window.title(f"{bloque}")
                # FRAMES -----------------------------------------------------------------
                reactivo = tk.Frame(edit_window)
                reactivo.grid(row=0,column=0,padx=5,pady=5)
                campos = tk.Frame(edit_window)
                campos.grid(row=1,column=0,padx=5,pady=5)
                botones_edit = tk.Frame(edit_window)
                botones_edit.grid(row=2,column=0,padx=5,pady=5)
                # COMBOBOX ----------------------------------------------------------------
                banners_var = tk.StringVar()
                # OPCIONES DE LOS BANNERS
                lista_banners = ['b1 BANNER DE PREPARACION ',
                                 'b2 BANNER DE EPP',
                                 'b3 BANNER DE PESE, CALCULE, ANOTE, AÑADA, TIRE',
                                 'b4 BANNER DE MEZCLAR EN 4 PARTES',
                                 'b5 BANNER DE advert. de explosion',
                                 'b6 ADVERTENCIA DEL TDI',
                                 'b7 CONSIDERACIONES BÁSICAS ANTES DE EMPEZAR EL PROCESO',
                                 'b8 MANTENGA LIMPIO SU REACTOR',
                                 'b9 PASE MUESTRA A CALIDAD'
                                 ]
                combo_productos = ttk.Combobox(edit_window, textvariable=banners_var, values=lista_banners)
                combo_productos.current(0)
                combo_productos.bind("<<ComboboxSelected>>", option_selected)
                combo_productos.grid(row=0, column=0)
                combo_banner = ttk.Label(edit_window,text=dict_producto[nombre_producto][bloque])
                combo_banner.grid(row=0,column=1,padx=5,pady=5)
                # BUTTONS ----------------------------------------------------------------
                guardar = ttk.Button(botones_edit,text="Guardar",command=save).grid(row=0, column=0,padx=5,pady=5)
                cerrar =  ttk.Button(botones_edit,text="Cerrar",command=cerrar).grid(row=0, column=1,padx=5,pady=5)
        selected_item = treeview.selection()  # Obtener el ítem seleccionado
        texto = treeview.item(selected_item[0], "text")
        tipo_bloque(texto)
    def eliminar_bloque():
        nonlocal dict_producto
        selected_item = treeview.selection()  # Obtener el ítem seleccionado

        bloque = treeview.item(selected_item[0], "text") 
        if selected_item:
            treeview.delete(selected_item[-1])  # Eliminar el último ítem seleccionado
        nombre_producto = name_prod_entry.get()
        del dict_producto[nombre_producto][bloque]
        messagebox.showwarning("Advertencia", f"Has borrado el bloque {bloque}")
    def anadir_bloque():
        nonlocal dict_producto
        seleccion = treeview.selection()
        if seleccion:
            # Prueba
            fourth_window = tk.Toplevel(third_window)
            fourth_window.title("Agregar Bloque")
            nuevo_bloque = {}
            def option_selected_x(event): # ESTA FUNCION ES PARA EL COMBOBOX: REACTIVO, PASO, BANNER
                selected_option = opciones_var.get()
                
                for widget in option_frames.values():
                    widget.grid_forget()

                if selected_option == lista_opciones[0]:# Reactivos
                    option_frames[lista_opciones[0]].grid(row=row, column=0, columnspan=2)
                elif selected_option == lista_opciones[1]:
                    option_frames[lista_opciones[1]].grid(row=row, column=0, columnspan=2)
                elif selected_option == lista_opciones[2]:
                    option_frames[lista_opciones[2]].grid(row=row, column=0, columnspan=2)

            def agregar_reactivo():# ESTA FUNCION AGARRA LA INFO EN LAS ENTRYBOXES DE REACTIVOS
        ##        nonlocal counter, treeview, treeview_data
                nonlocal dict_producto, entries
                data = []
                for i,entry in enumerate(entries):
                    data.append(entry.get())
                nombre_producto = name_prod_entry.get()
                claves = list(dict_producto[nombre_producto].keys())
                claves.insert(int(seleccion[0])-1,data[0])
                dict_prod = {}
                for i,clave in enumerate(claves):
                    if clave == data[0]:
                        dict_prod[clave] = {"descripcion":data[1],
                                            "peligro":data[2],
                                            "indicacion":data[3],
                                            "revision":data[4]} 
                    else:
                        dict_prod[clave] = dict_producto[nombre_producto][clave]
                treeview.delete(*treeview.get_children())
                for i,item in enumerate(dict_prod):
                    treeview.insert(parent="", index="end", iid=i+1, text=item, values = ("",""), open=True)
                fourth_window.destroy()
                # GUARDAMOS LOS CAMBIOS AHORA SI EN EL PRINCIPAL
                dict_producto[nombre_producto] = dict_prod
                messagebox.showwarning("Advertencia", f"Has agregado el reactivo {data[0]}")

            def agregar_paso():
                nonlocal dict_producto, paso_texto # utiliza el la variable que esta afuera de este metodo
                dict_prod = {} # CREAMOS UN NUEVO DICCIONARIO DONDE AGREGAREMOS LA ANTERIORES BLOQUES JUNTO CON EL NUEVO EN SU RESPECTIVO ORDEN
                counter = 1 # SE EMPIEZA UN NNUEVO CONTEO DE LOS PASOS
                texto = paso_texto.get(1.0, "end-1c") # SE OBTIENE EL TEXTO DEL ENTRY
##                print(texto)# NOS ASEGURAMOS DEL TEXTO CON UN INDICADOR
                nombre_producto = name_prod_entry.get()# OBTENEMOS EL NOMBRE DEL PRODUCTO QUE ESTAMOS MODIFICANDO
                claves = list(dict_producto[nombre_producto].keys())# OBTENEMOS TODOS LAS KEYS DE ESE PRODUCTO
##                print(f'seleccion {seleccion[0]}')# MOSTRAMOS LA POSICION LA CUAL QUEREMOS METER POR DEBAJO LA OPCION
                control_pasos = []
                for j,clave in enumerate(claves):# POR CADA NOMBRE DE LAS CLAVES...
                    if clave[0] == "P":
                        claves[j] = f"Paso {counter}"
                        counter += 1
                    if j == int(seleccion[0])-1:# EN LA POSICION SIGUIENTE DE LA UBICACION ELEGIDA
                        nuevo_paso = f'Paso {counter}'
                        
                        messagebox.showwarning("Advertencia", f"Has agregado el reactivo {nuevo_paso}")
                        claves.insert(int(seleccion[0])-1,nuevo_paso)# AGREGAMOS EL "PASO" EN SU CORRESPONDIENTE ORDEN
                        counter += 1
                    
                for i,clave in enumerate(claves):
                    if clave == nuevo_paso:
                        dict_prod[clave] = {"texto":texto}
                    else:
                        try:
                            dict_prod[clave] = dict_producto[nombre_producto][clave]
                        except:
                            last_clave = clave[0:len(clave)-2]+' '+str(int(clave[-1])-1)
                            dict_prod[clave] = dict_producto[nombre_producto][last_clave]
                # AQUI YA SE AÑADIO TODO BIEN
                treeview.delete(*treeview.get_children())
                for i,item in enumerate(dict_prod):
##                    print(f'Item#{i} : {item}')
                    treeview.insert(parent="", index="end", iid=i+1, text=item, values = ("",""), open=True)
                fourth_window.destroy()
                # GUARDAMOS LOS CAMBIOS AHORA SI EN EL PRINCIPAL
                dict_producto[nombre_producto] = dict_prod
                
            def agregar_banner():
                nonlocal dict_producto, paso_texto # utiliza el la variable que esta afuera de este metodo
                dict_prod = {} # CREAMOS UN NUEVO DICCIONARIO DONDE AGREGAREMOS LA ANTERIORES BLOQUES JUNTO CON EL NUEVO EN SU RESPECTIVO ORDEN
                counter = 1 # SE EMPIEZA UN NNUEVO CONTEO DE LOS PASOS
                selected_option = banners_var.get()
##                print(selected_option)# NOS ASEGURAMOS DEL TEXTO CON UN INDICADOR
                nombre_producto = name_prod_entry.get()# OBTENEMOS EL NOMBRE DEL PRODUCTO QUE ESTAMOS MODIFICANDO
                claves = list(dict_producto[nombre_producto].keys())# OBTENEMOS TODOS LAS KEYS DE ESE PRODUCTO
##                print(f'seleccion {seleccion[0]}')# MOSTRAMOS LA POSICION LA CUAL QUEREMOS METER POR DEBAJO LA OPCION
                for j,clave in enumerate(claves):# POR CADA NOMBRE DE LAS CLAVES...
##                    print(clave)# VEMOS EL ORDEN DE LAS COSAS SEGUN LA CLAVE
                    if clave[0] == "B":
                        claves[j] = f"Banner {counter}"
                        counter += 1
##                        print(f'>>> Paso {counter}')# MOSTRAMOS QUE SI CONTAMOS LOS PASOS
                    if j == int(seleccion[0])-1:# EN LA POSICION SIGUIENTE DE LA UBICACION ELEGIDA
                        nuevo_banner = f'Banner {counter}'
                        messagebox.showwarning("Advertencia", f"Has agregado el reactivo {nuevo_banner}")
                        claves.insert(int(seleccion[0])-1,nuevo_banner)# AGREGAMOS EL "PASO" EN SU CORRESPONDIENTE ORDEN
                        counter += 1
                    
##                print(claves)
                for i,clave in enumerate(claves):
##                    print(f'Clave : {clave}')
                    if clave == nuevo_banner:
                        dict_prod[clave] =selected_option[0:2]
                    else:
                        try:
                            dict_prod[clave] = dict_producto[nombre_producto][clave]
                        except:
                            last_clave = clave[0:len(clave)-2]+' '+str(int(clave[-1])-1)
                            dict_prod[clave] = dict_producto[nombre_producto][last_clave]
##                print(dict_prod)
                # AQUI YA SE AÑADIO TODO BIEN
                treeview.delete(*treeview.get_children())
                for i,item in enumerate(dict_prod):
##                    print(f'Item#{i} : {item}')
                    treeview.insert(parent="", index="end", iid=i+1, text=item, values = ("",""), open=True)
                fourth_window.destroy()
                # GUARDAMOS LOS CAMBIOS AHORA SI EN EL PRINCIPAL
                dict_producto[nombre_producto] = dict_prod
                
                
            opciones_var = tk.StringVar()
            option_frames = {}      # DICCIONARIO : AQUI GUARDAN WIDGETS TIPO FRAME
            row = 6                 # ULTIMA FILA LIBRE DESPUES DE LOS CAMPOS DE NOMBRE, NO DE INV, Y PICTOGRAMAS
            # --COMBOBOX-------------------------------------------------------------------------------------------------------------------------------------------------
            lista_opciones = ['reactivo','texto','banner']
            opciones = ttk.Combobox(fourth_window, textvariable=opciones_var, values=lista_opciones)
            opciones.current(0)
            opciones.bind("<<ComboboxSelected>>", option_selected_x)
            opciones.grid(row=0, column=0,padx=10,pady=10)
            # --COMBOBOX------------------------------------------------OPCION 1-----------------------------------------------------------------------------------------
            ############# Option 1 content                                                                      #REACTIVO
            option_frames[lista_opciones[0]] = tk.Frame(fourth_window) # CAMPOS DE LA OPCION 1 "REACTIVOS"
            specs = ['No. Inv.','descripcion','pictogramas','indicaciones','revision']
            # LISTA DONDE SE GUARDA LAS VARIABLES INGRESADAS EN LOS ENTRIES DE LA OPCION 1
            entries = []
            for i,j in enumerate(specs):# PARA CADA ESPECIFICACION DE "REACTIVOS"...
                tk.Label(option_frames[lista_opciones[0]], text=j).grid(row=i, column=0)# AÑADES AL FRAME "REACTIVOS" UNA ETIQUETA...
                entry = tk.Entry(option_frames[lista_opciones[0]])# AÑADES AL FRAME "REACTIVOS" UN ENTRY...
                entry.grid(row=i, column=1)# SE POSICIONA EL ENTRY...
                entries.append(entry)# ESTE ENTRY TAMBIEN SE AÑADE A # LISTA DONDE SE GUARDA LAS VARIABLES INGRESADAS EN LOS ENTRIES DE LA OPCION 1
            # BOTON QUE AGREGA LA INFORMACION DE LOS CAMPOS DE LA OPCION REACTIVOS" AN TREEVIEW Y PROXIMAMENTE AL ARCHIVO 
            tk.Button(option_frames[lista_opciones[0]],text="agregar",command=agregar_reactivo).grid(row=row+len(specs), column=0) 
            # --COMBOBOX------------------------------------------------OPCION 2-----------------------------------------------------------------------------------------
            ############# Option 2 content                                                                      # TEXTO
            option_frames[lista_opciones[1]] = tk.Frame(fourth_window)
            tk.Label(option_frames[lista_opciones[1]], text="Agregar texto").grid(row=0, column=0)# ETIQUETA
            paso_texto = tk.Text(option_frames[lista_opciones[1]],width=30,height=10)# WIDGET DE TEXTO
            paso_texto.grid(row=0, column=1)# POSICION DEL WIDGET
            # BOTON QUE AGREGA EL TEXTO AL TREEVIEW
            tk.Button(option_frames[lista_opciones[1]],text="agregar",command=agregar_paso).grid(row=row+len(specs), column=0)
            # --COMBOBOX------------------------------------------------OPCION 3-----------------------------------------------------------------------------------------
            ############# Option 3 content                                                                      # BANNER
            option_frames[lista_opciones[2]] = tk.Frame(fourth_window)
            banners_var = tk.StringVar()
            # OPCIONES DE LOS BANNERS
            lista_banners = ['b1 BANNER DE PREPARACION ',
                             'b2 BANNER DE EPP',
                             'b3 BANNER DE PESE, CALCULE, ANOTE, AÑADA, TIRE',
                             'b4 BANNER DE MEZCLAR EN 4 PARTES',
                             'b5 BANNER DE advert. de explosion',
                             'b6 ADVERTENCIA DEL TDI',
                             'b7 CONSIDERACIONES BÁSICAS ANTES DE EMPEZAR EL PROCESO',
                             'b8 MANTENGA LIMPIO SU REACTOR',
                             'b9 PASE MUESTRA A CALIDAD'
                             ]
            tk.Label(option_frames[lista_opciones[2]], text="Agregar Banner").grid(row=row, column=0)# ETIQUETA 
            banner_combo = ttk.Combobox(option_frames[lista_opciones[2]], textvariable=banners_var, values=lista_banners)# MENU COMBOBOX
            banner_combo.current(0)
            banner_combo.grid(row=row, column=1)
            # BOTON QUE AGREGA EL TEXTO AL TREEVIEW
            ttk.Button(option_frames[lista_opciones[2]],text="agregar",command=agregar_banner).grid(row=row+len(specs), column=0)
            # BOTON QUE AGREGA NUEVO BANNER
            ttk.Button(option_frames[lista_opciones[2]],text="agregar",command=agregar_n_banner).grid(row=row+len(specs), column=1)

    # -------------------------------------------------------------------------------------- FRAMES ----------------------------------------------------------------
    third_window = tk.Toplevel(root)
    third_window.title("Editar metodo de Fabricación")
    data_n_tree = tk.Frame(third_window,bg="#ffffff") # 1 (0,0)
    data_n_tree.grid(row=0,column=0)
    botones = tk.Frame(third_window)# 1 (1,0)
    botones.grid(row=1,column=0)# 
    datos = tk.Frame(data_n_tree)# 2 (0,0)
    datos.grid(row=0,column=0)
    d1 = ttk.LabelFrame(datos,text="Datos del producto")# 3 (0,0)
    d1.grid(row=0,column=0,padx = 2, pady = 2)
    d2 = tk.Frame(datos)# 3 (1,0)
    d2.grid(row=1,column=0)
    d3 = ttk.LabelFrame(datos,text="Bloques")# 3 (2,0)
    d3.grid(row=2,column=0)
    d4 = ttk.LabelFrame(d1,text="Equipo a utilizar")# 4 (6,0)
    d4.grid(row=6,column=0)
    label = ttk.LabelFrame(datos, text="Crear Metodo de Fabricación Estandar")# 3 (0,0)
    label.grid(row=0, column=0)
    # ------VARIABLES QUE CONTABILIZAN LOS BLOQUES DE TEXTO Y DE BANNERS--------------------------------------------------------------------------------------------------

    producto_actual = {}
    counter = 1             # CUENTA CUANTOS ELEMENTOS HAY EN EL 
    counter_paso = 1        # CUENTA EL NUMERO DE PASOS QUE HAY AGREGADOS AL TREEVIEW
    counter_banner = 1      # CUENTA EL NUMERO DE BANNERS QUE HAY AGREGADOS AL TREEVIEW
    treeview_data = []      # DONDE SE GUARDA LA INFORMACION MOSTRADA EN EL TREEVIEW    
    element_counter = []    # LISTA DE REGISTRO CUANDO SE AGREGA UN BANNER "b" O UN PASO "p"
    
    # -------------------------------------COMBOBOX------------------------------------------------------------------------------------------------------------------
    lista_productos = []
##    productos_reactivos = Productos()
    with open('datos.json', 'r') as archivo:# extraer la info previa
        datos_cargados = json.load(archivo)# antigua info
    for i,producto in enumerate(datos_cargados):
        lista_productos.append(producto)
    
    combo_productos = ttk.Combobox(d1, textvariable=combo_productos_var, values=lista_productos)
    combo_productos.current(0)
    combo_productos.bind("<<ComboboxSelected>>", option_selected)
    combo_productos.grid(row=0, column=1)    
    
    lista_treeview = mostrar_lista(datos_cargados)# PARA ESTA FUNCION REQUIERE QUE SEA UN DICCIONARIO ?

    # ------WIDGETS-------------------------------------------------------------------------------------------------------------------------------------------------------
        # NOMBRE DEL PRODUCTO                                           ENTRYS Y LABELS
    # ETIQUETA
    name_prod = tk.Label(d1, text="Nombre del productos", font=('Arial', 9),bg="#ffffff",fg="#000000")
    name_prod.grid(row=1, column=0)
    # ENTRY        
    name_prod_entry = ttk.Entry(d1,font=("Helvetica",15))
    name_prod_entry.grid(row=1, column=1)
    # ----------------------------------------------------------------------
        # NO DE INVENTARIO
    # ETIQUETA
    no_prod = tk.Label(d1, text="No. Inv.", font=('Arial', 9),bg="#ffffff",fg="#000000")
    no_prod.grid(row=2, column=0)
    # ENTRY                    
    no_prod_entry = ttk.Entry(d1,font=("Helvetica",15))
    no_prod_entry.grid(row=2, column=1)
    # ----------------------------------------------------------------------
        # PICTOGRAMA DEL PRODUCTO
    # ETIQUETA
    picto_prod = tk.Label(d1, text="Str pictogramas max 3", font=('Arial', 9),bg="#ffffff",fg="#000000")
    picto_prod.grid(row=3, column=0)
    # ENTRY                    
    picto_prod_entry = ttk.Entry(d1,font=("Helvetica",15))
    picto_prod_entry.grid(row=3, column=1)
    # ----------------------------------------------------------------------
        # ENVASE 
    # ETIQUETA
    etiq_prod = tk.Label(d1, text="Envasar en: ", font=('Arial', 9),bg="#ffffff",fg="#000000")
    etiq_prod.grid(row=4, column=0)
    # ENTRY                    
    etiq_prod_entry = ttk.Entry(d1,font=("Helvetica",15))
    etiq_prod_entry.grid(row=4, column=1)
    # ----------------------------------------------------------------------
        # PASAR MUESTRA EN 
    # ETIQUETA
    mues_prod = tk.Label(d1, text="Pasar Muestra en: ", font=('Arial', 9),bg="#ffffff",fg="#000000")
    mues_prod.grid(row=5, column=0)
    # ENTRY                    
    mues_prod_entry = ttk.Entry(d1,font=("Helvetica",15))
    mues_prod_entry.grid(row=5, column=1)
    # ----------------------------------------------------------------------
        # EQUIPO A UTILIZAR
    # ETIQUETA
    equi_labe = tk.Label(d1, text="Equipo a utilizar: ", font=('Arial', 9),bg="#ffffff",fg="#000000")
    equi_labe.grid(row=6, column=0)
    # ENTRY                    
    equi_labe_entry = ttk.Entry(d1,font=("Helvetica",15))
    equi_labe_entry.grid(row=6, column=1)
    # ----------------------------------------------------------------------
        # MALLA
    # ETIQUETA
    mall_labe = tk.Label(d1, text="Malla a utilizar: ", font=('Arial', 9),bg="#ffffff",fg="#000000")
    mall_labe.grid(row=7, column=0)
    # ENTRY                    
    mall_labe_entry = ttk.Entry(d1,font=("Helvetica",15))
    mall_labe_entry.grid(row=7, column=1)
    # --------------------------------------------------------------BOTONES DE EDICION-----------------------------------------------------------------
    edit_boton = ttk.Button(botones,text="Editar bloque",command=editar_bloque)
    edit_boton.grid(row=0, column=0)
    edit_boton.bind("<Return>", on_enter)
    dele_boton = ttk.Button(botones,text="Eliminar bloque",command = eliminar_bloque)
    dele_boton.grid(row=0, column=1)
    dele_boton.bind("<Return>", on_enter)
    add_boton = ttk.Button(botones,text="añadir bloque",command=anadir_bloque)
    add_boton.grid(row=0, column=2)
    add_boton.bind("<Return>", on_enter)
    guar_boton = ttk.Button(botones,text="Guardar metodo",command=save_method)
    guar_boton.grid(row=0, column=3)
    guar_boton.bind("<Return>", on_enter)
    # --------------------------------------------------------------TREEVIEW-----------------------------------------------------------------------------
    # Create a Frame for the Treeview
    treeFrame = ttk.Frame(data_n_tree)
    treeFrame.grid(row=0, column=1)

    # Scrollbar
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side="right", fill="y")

    # Treeview
    treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1, 2), height=12)
    treeview.pack(expand=True, fill="both")
    treeScroll.config(command=treeview.yview)

    # Treeview columns
    treeview.column("#0", width=100)
    treeview.column(1, anchor="w", width=100)
    treeview.column(2, anchor="w", width=100)
    
    # Treeview headings
    treeview.heading("#0", text="Nombre", anchor="center")
    treeview.heading(1, text="Descripcion", anchor="center")
    treeview.heading(2, text="Pictogramas", anchor="center")
    # Hacer que la nueva ventana sea activa
    third_window.focus_force()
