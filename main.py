import sys
import os
import json
import tkinter as tk
from inflacion import inflacion  # tu módulo local

# Colores
black = "#000000"
yellow = "#ffd900"
logo_color = "#40fea6"
green = '#3b9c34'
white = '#ffffff'

# ---------------- Funciones ----------------
def calc(e):
    try:
        costo = round(float(costo_unitario.get()), 2)
        comision_deseada = round(float(comision.get()), 2)
        impuesto = round(float(iva.get()), 2)
        desc = round(float(descuento.get()), 2)
        if costo > 0 and 0 <= comision_deseada <= 99:
            if impuesto < 0 or desc < 0: return

            pas1 = 100 - comision_deseada
            pas2 = pas1 / 100
            pas3 = costo / pas2
            pas4 =  pas3 * (desc / 100)
            pas5 = pas3 - pas4
            result = pas5
            earning = result - costo
            
            t = result * (impuesto / 100)
            valor_final = result + t 
                 

            subtotal.config(text=f'Subtotal: {result:,.2f}')
            margen_descuento.config(text=f'Descuento: %{desc:,.2f}')
            if earning < 0:
                ganancia.config(text=f'Pérdida: {earning:,.2f}', bg="#db1d1d", fg='#ffffff', font=('Arial', 15, 'bold'))
            else:
                ganancia.config(text=f'Ganancia: +{earning:,.2f}', bg=white, fg=black, font=('Arial', 15))
                
            
            # IMPUESTOS

            margin_earning = round((earning / result) * 100, 2)
            margin_cost = round(((valor_final - costo) / costo) * 100, 2)
            
            margen_de_ganancia.config(text=f'Margen de ganancia: %{margin_earning}')
            margen_sobre_costo.config(text=f'Margen sobre costo: %{margin_cost:,.2f}')

            gobierno = round(((valor_final - result) / result) * 100, 2)
            total.config(text=f'Precio: {valor_final:,.2f}')
            margen_iva.config(text=f'IVA: %{gobierno:,.2f}')


            # Historial
            data = {
                'comision': comision_deseada,
                'iva': impuesto,
                'descuento': desc
            }
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)

    except ValueError:
        subtotal.config(text='')
        ganancia.config(text='')
        margen_de_ganancia.config(text='')  
        margen_sobre_costo.config(text='')
        total.config(text='')
        margen_iva.config(text='')
        margen_descuento.config(text='')
        pass

# ---------------- Ventana principal ----------------
ventana = tk.Tk()
ventana.title('CEI - Calculate earnings and inflation')
ventana.minsize(780, 500)
ventana.config(bg=white)
ventana.columnconfigure(0, weight=1)

# ---------------- Header ----------------
header = tk.Frame(ventana, bg='black')
header.grid(row=0, column=0, sticky='ew')
header.columnconfigure(0, weight=1)

logo = tk.Label(header, text='CEI', bg='black', fg=yellow, font=('', 17, 'bold'))
logo.grid(row=0, column=0, padx=15, pady=15, sticky='w')

open_inflation = tk.Button(header, text='Inflación', font=('Arial', 13 ,'bold'), bg=black, fg='#ffffff')
open_inflation.grid(row=0, column=1, padx=15, pady=15)
open_inflation.config(command=inflacion)

version = tk.Label(header, text='Version 1.0.0', fg='white', bg='black')
version.grid(row=0, column=2, padx=15, pady=15, sticky='e')

# ---------------- Contenedor para Labels+Entries ----------------
frame_inputs = tk.Frame(ventana, bg=white)
frame_inputs.grid(row=1, column=0, padx=15, pady=15, sticky='w')

# Costo Unitario
frame_costo = tk.Frame(frame_inputs)
frame_costo.grid(row=0, column=0)
label_costo_unitario = tk.Label(frame_costo, text='Costo Unitario', font=('Arial', 14))
label_costo_unitario.pack(anchor='w')
costo_unitario = tk.Entry(frame_costo, font=('Arial', 13), bd=1)
costo_unitario.pack(anchor='w', pady=5)

# Comisión
frame_comision = tk.Frame(frame_inputs)
frame_comision.grid(row=0, column=1, padx=20)
label_comision = tk.Label(frame_comision, text='Comisión %', font=('Arial', 14))
label_comision.pack(anchor='w')
comision = tk.Entry(frame_comision, font=('Arial', 13), bd=1)
comision.pack(anchor='w', pady=5)

# IVA
frame_iva = tk.Frame(frame_inputs)
frame_iva.grid(row=0, column=2, padx=20)
label_iva = tk.Label(frame_iva, text='IVA (impuesto) %', font=('Arial', 14))
label_iva.pack(anchor='w')
iva = tk.Entry(frame_iva, font=('Arial', 13), bd=1)
iva.pack(anchor='w', pady=5)


# Descuento
frame_descuento = tk.Frame(frame_inputs)
frame_descuento.grid(row=1, column=0, padx=20)
label_descuento = tk.Label(frame_descuento, text='Descuento %', font=('Arial', 14))
label_descuento.pack(anchor='w')
descuento = tk.Entry(frame_descuento, font=('Arial', 13), bd=1)
descuento.pack(anchor='w', pady=5)

file_json = 'data.json'
if os.path.exists(file_json):
    with open(file_json, 'r') as f:
        data = json.load(f)        
        comision.insert(0, data['comision'])
        iva.insert(0, data['iva'])
        descuento.insert(0, data['descuento'])
else:
    print('No existe el Json')

# ---------------- Resultados ----------------
frame_total = tk.Frame(ventana, bg=white)
frame_total.grid(row=2, column=0, sticky='w', padx=15, pady=10)

margen_descuento = tk.Label(frame_total, font=('Arial', 15), bg=white)
margen_descuento.grid(row=0, column=0, sticky='w')

ganancia = tk.Label(frame_total, font=('Arial', 15), bg=white)
ganancia.grid(row=0, column=1, sticky='w', padx=15)

subtotal = tk.Label(frame_total, font=('Arial', 15, 'bold'), bg=white)
subtotal.grid(row=0, column=2, sticky='w')

margen_de_ganancia = tk.Label(ventana, font=('Arial', 13), bg=white)
margen_de_ganancia.grid(row=3, column=0, sticky='w', padx=15, pady=5)
margen_sobre_costo = tk.Label(ventana, font=('Arial', 13), bg=white)
margen_sobre_costo.grid(row=4, column=0, sticky='w', padx=15, pady=5)
margen_iva = tk.Label(ventana, font=('Arial', 13), bg=white)
margen_iva.grid(row=5, column=0, sticky='w', padx=15, pady=5)
total = tk.Label(ventana, font=('Arial', 17, 'bold'), bg=white)
total.grid(row=6, column=0, sticky='w', padx=15, pady=15)

# ---------------- Eventos ----------------
costo_unitario.bind("<KeyRelease>", calc)
comision.bind("<KeyRelease>", calc)
iva.bind("<KeyRelease>", calc)
descuento.bind('<KeyRelease>', calc)

ventana.mainloop()