

import tkinter as tk
from tkinter import ttk
##from productos_reactivos import Productos
from tkinter import messagebox
import json
from just_the_module import Save_module
import opcion_crear
import opcion_editar
from color_window import Color_selector
from PIL import Image, ImageTk
import time



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2 
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
def on_enter(event):
    event.widget.invoke()  # Simular clic en el botón al presionar Enter

# QUE APRENDIMOS EL DIA DE HOY
# APRENDI. A INVOCAR MULTIPLES VENTANAS EN TKINTER
# A HACER QUE APAREZCAN MULTIPLES WIDGETS EN  UNA MISMA VENTANA
# A USAR UNA VARIABLE QUE NO ESTA AL MISMO NIVEL DEL FUNCION (NONLOCAL)
# A COMO USAR LA INFORMACION DENTRO DE LOS WIDGETS
# QUE SI SE PUEDE USAR UNA FUNCION DENTRO DE OTRA FUNCION

# QUE APRENDIMOS EL DIA DE HOY
# APRENDI A DARLE MAS FORMATO A LA INTERFAZ USANDO MAS FRAMES Y LABEL FRAMES
# COMPLETE EL AÑADIDO DE BANNER Y PASOS AL TREEVIEW

# EL RETO ES EXTRAER LA INFO Y ESCRIBIRLA EN producto_reactivos.py

# Buscar el metodo de fabricacion del TC9 43AT
def abrir_menu_crear():
    opcion_crear.crear(root)
    actualizar.config(bg="Yellow")
def editar_menu():
    opcion_editar.editar(root)
    actualizar.config(bg="Yellow")
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
            treeview_data.append(("","end",counter,producto))# ("a","b")
                # SE GUARDA EL NUMERO DE CONTEO
            childof = counter
            for k,data in enumerate(diccionario[producto]):
                counter += 1
                treeview_data.append((childof,"end",counter,data))
        return treeview_data

def destroy():
    root.destroy()
def excelizar():
    seleccion = treeview.selection()
    if seleccion:
        item = treeview.get_children()
        for i,j in enumerate(treeview.get_children()):
            if seleccion[0] in treeview.get_children():
                index = i
        producto = treeview.item(int(seleccion[0]))['text']
        print(producto)
        with open('datos.json', 'r') as archivo:# extraer la info previa
            datos_cargados = json.load(archivo)
        no = datos_cargados[producto]["Informacion"]["no inv"]
        diccionario_producto = {}
        diccionario_producto[producto] = datos_cargados[producto]
        f = Save_module()
        f.active_module(producto,no,diccionario_producto)
def actualizar():
    
    actualizar.config(bg="LightBlue")
    with open('datos.json', 'r') as archivo:# extraer la info previa
        treeview_datan.clear()
        treeview_datan.update(json.load(archivo))
    for item in treeview.get_children():
        treeview.delete(item)
    treeview_data = mostrar_lista(treeview_datan)
    for item in treeview_data:
        treeview.insert(parent=item[0], index=item[1], iid=item[2], text=item[3])
def eliminar():
    selected_item = treeview.selection()  # Obtener el ítem seleccionado selected_item
    if selected_item:
        # Obtener valores de la fila seleccionada
        fila_seleccionada = treeview.item(selected_item[0])['text']
        treeview.delete(selected_item[-1])  # Eliminar el último ítem seleccionado
        # ESTO UNICAMENTE ELIMINA EL ELEMENTO DE
        with open('datos.json', 'r') as archivo:# extraer la info previa
            datos_cargados = json.load(archivo)# antigua info
        del datos_cargados[fila_seleccionada]
        
        with open('datos.json', 'w') as archivo:
            json.dump(datos_cargados,archivo)

    
#### ---------------------------------------------------------------------- MAIN WINDOW ---------------------------------------------------------------------------####    



def mostrar_gif_y_ejecutar_despues():
    def cargar_gif():
        def animar_gif(gif, indice):
            try:
                # Obtener el siguiente fotograma
                gif.seek(indice)
                nuevo_fotograma = ImageTk.PhotoImage(gif)

                # Actualizar la etiqueta con el nuevo fotograma
                etiqueta_gif.config(image=nuevo_fotograma)
                etiqueta_gif.image = nuevo_fotograma

                # Programar la llamada recursiva para el siguiente fotograma
                ventana.after(5, animar_gif, gif, indice + 1)
            except EOFError:
                # Reiniciar la animación al llegar al final del GIF
                ventana.after(5000, ventana.destroy)  # Cierra la ventana después de 10 segundos
        ruta_gif = "images/P.E.T.R.A. MeTHOD GEN.gif"  # Reemplaza "ruta_del_archivo.gif" con la ruta de tu archivo GIF
        gif = Image.open(ruta_gif)
        # Redimensionar el GIF para hacerlo más pequeño
        gif = gif.resize((470, 394), Image.LANCZOS)
        fotograma = ImageTk.PhotoImage(gif)

        # Configurar etiqueta para mostrar el GIF
        etiqueta_gif.config(image=fotograma)
        etiqueta_gif.image = fotograma

        # Iniciar la animación llamando a la función después de un tiempo
        ventana.after(0, animar_gif, gif, 1)


    # Configuración de la ventana principal
    ventana = tk.Tk()

    # Etiqueta para mostrar el GIF
    etiqueta_gif = ttk.Label(ventana)
    etiqueta_gif.pack(pady=10)

    # Llamar a la función para cargar y mostrar el GIF automáticamente
    ventana.after(0, cargar_gif)

    ventana.mainloop()

# Llama a la función principal
mostrar_gif_y_ejecutar_despues()
time.sleep(1)

root = tk.Tk()
root.config(bg="#000000")
root.title("PETRA: GENERADOR DE METODOS")
root.option_add("*tearOff", False) # This is always a good idea
# Make the app responsive
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)

# Create a style
style = ttk.Style(root)

# Create lists for the Comboboxes
option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]

# Create control variables
a = tk.BooleanVar()
b = tk.BooleanVar(value=True)
c = tk.BooleanVar()
d = tk.IntVar(value=2)
e = tk.StringVar(value=option_menu_list[1])
f = tk.BooleanVar()
g = tk.DoubleVar(value=75.0)
h = tk.BooleanVar()


# Create a Frame for input widgets
widgets_frame = tk.Frame(root)
widgets_frame.config(bg="#000000")
widgets_frame.grid(row=0, column=0, padx=10, pady=(30, 10), sticky="nsew", rowspan=3)
widgets_frame.columnconfigure(index=0, weight=1)
# ------BOTONES-------------------------------------------------------------------------------------------------------------------------------------------------------
# Button
crear = tk.Button(widgets_frame, text="Crear un metodo de Fabricación", command=abrir_menu_crear,bg="#ea00d9",fg="Black",font=("System", 12, "bold"))
crear.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
crear.bind("<Return>", on_enter)
editar = tk.Button(widgets_frame, text="Editar un metodo existente", command = editar_menu,bg="#0abdc6",fg="Black",font=("System", 12, "bold"))
editar.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
editar.bind("<Return>", on_enter)
eliminar = tk.Button(widgets_frame, text="Eliminar Producto", command=eliminar,bg="Red",fg="White",font=("System", 12, "bold"))
eliminar.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
eliminar.bind("<Return>", on_enter)
excelizar = tk.Button(widgets_frame, text="Excelizar Metodo", command=excelizar,bg="#2d572c",fg="White",font=("System", 12, "bold"))
excelizar.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")
excelizar.bind("<Return>", on_enter)
actualizar = tk.Button(widgets_frame, text="Actualizar", command=actualizar,bg="#133e7c",fg="White",font=("System", 12, "bold"))
actualizar.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")
# Accentbutton
accentbutton = tk.Button(widgets_frame, text="Terminar programa", command=destroy,bg="Red",fg="White",font=("System", 12, "bold"))
accentbutton.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")
accentbutton.bind("<Return>", on_enter)
# ------TREEVIEW------------------------------------------------------------------------------------------------------------------------------------------------------
# Panedwindow
paned = ttk.PanedWindow(root)
paned.grid(row=0, column=1, pady=(25, 5), sticky="nsew", rowspan=3)

# Pane #1
pane_1 = ttk.Frame(paned)
paned.add(pane_1, weight=1)

# Create a Frame for the Treeview
treeFrame = ttk.Frame(pane_1)
treeFrame.pack(expand=True, fill="both", padx=5, pady=5)

# Scrollbar
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

# Treeview
treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, height=12)
treeview.pack(expand=True, fill="both")
treeScroll.config(command=treeview.yview)

# Treeview columns
treeview.column("#0", width=200)

# Treeview headings
treeview.heading("#0", text="Column 1", anchor="center")

# --EXTRACCION DE DATOS: JSON----------------------------------------------------------------
with open('datos.json', 'r') as archivo:# extraer la info previa
            treeview_datan = json.load(archivo)# antigua info
treeview_data = mostrar_lista(treeview_datan)
for item in treeview_data:
    treeview.insert(parent=item[0], index=item[1], iid=item[2], text=item[3])


# Select and scroll
treeview.selection_set(10)
estilo = ttk.Style()

# Cambiar el color del Scrollbar vertical
estilo.configure("Vertical.TScrollbar", troughcolor="lightblue", background="Black", gripcount=10, gripcolor="white")

# Cambiar el color del fondo de los headings
estilo.configure("Treeview.Heading", background="Blue", foreground="black")
estilo.configure("Treeview", background="#0abdc6",foreground="Black")


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Sizegrip
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))

# Center the window, and set minsize
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

# Start the main loop
root.mainloop()
