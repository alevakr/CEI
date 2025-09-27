import tkinter as tk

def inflacion():
    page = tk.Toplevel()
    page.minsize(440, 600)
    page.title('Calcular inflación')
    page.columnconfigure(0, weight=1)

    # Título
    label = tk.Label(page, text='Calculadora de inflación', font=('Arial', 18))
    label.grid(row=0, column=0, pady=30, padx=15)

    # Valor actual
    label_precio_actual = tk.Label(page, text='Valor Actual', font=('', 15))
    label_precio_actual.grid(row=1, column=0, sticky='w', pady=(10, 5), padx=15)

    precio_actual = tk.Entry(page, font=('Arial', 13), bd=0)
    precio_actual.grid(row=2, column=0, sticky='w', pady=(0, 20), padx=15)

    # Valor anterior
    label_precio_anterior = tk.Label(page, text='Valor Anterior', font=('', 15))
    label_precio_anterior.grid(row=3, column=0, sticky='w', pady=(10, 5), padx=15)

    precio_anterior = tk.Entry(page, font=('Arial', 13), bd=0)
    precio_anterior.grid(row=4, column=0, sticky='w', pady=(0, 30), padx=15)

    # Resultados
    frame_main = tk.Frame(page)
    frame_main.grid(row=5, column=0, sticky='w', pady=10, padx=20)

    markup = tk.Label(frame_main, font=('', 14))
    markup.pack(side='left')

    result = tk.Label(frame_main)
    result.pack(side='left', padx=50)

    # Cálculo
    def inflation(e):
        try:
            a = float(precio_actual.get())
            b = float(precio_anterior.get())
            if a > 0 and b > 0:
                calc = round(((a - b) / b) * 100, 2)
                r = round(a - b, 2)
                markup.config(text=f'Inflación: %{calc:,.2f}')

                if calc > 0:
                    result.config(text=f'+{r:,.2f}', fg='#ffffff', bg="#ce0000", font=('', 15, 'bold'))
                else:
                    result.config(text=f'{r:,.2f}', fg='#ffffff', bg="#3b9c34", font=('', 15, 'bold'))
        except ValueError:
            markup.config(text='', bg='#ffd900')
            result.config(text='')

    precio_actual.bind('<KeyRelease>', inflation)
    precio_anterior.bind('<KeyRelease>', inflation)
