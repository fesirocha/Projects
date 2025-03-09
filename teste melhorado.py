from tkinter import *

# Configurando o app ---------------------
app = Tk()
app.title('Cronômetro')
app.geometry('300x180')
app.config(bg='black')
app.resizable(width=False, height=False)

# Variáveis globais ----------------------
tempo = "00:00:00"
rodar = False
segundos = 0
id_after = None  # Identificador da chamada after()

# Função para iniciar o cronômetro --------
def iniciar():
    global segundos, rodar, id_after

    if rodar:
        # Convertendo segundos para horas, minutos e segundos
        h = segundos // 3600
        m = (segundos % 3600) // 60
        s = segundos % 60

        # Atualizando o texto do cronômetro
        tempo_formatado = f"{h:02}:{m:02}:{s:02}"
        label_tempo.config(text=tempo_formatado)

        # Incrementando o tempo
        segundos += 1
        id_after = label_tempo.after(1000, iniciar)  # Guardar a referência do after()

# Função para dar início ao cronômetro ----
def start():
    global rodar, id_after
    if not rodar:
        rodar = True
        if id_after:  # Cancela qualquer chamada pendente de after
            app.after_cancel(id_after)
        iniciar()

# Função para pausar ---------------------
def pausar():
    global rodar, id_after
    rodar = False
    if id_after:  # Cancela a chamada pendente do after
        app.after_cancel(id_after)
        id_after = None

# Função para reiniciar ------------------
def reiniciar():
    global segundos, rodar, id_after
    rodar = False
    segundos = 0
    label_tempo.config(text="00:00:00")
    if id_after:
        app.after_cancel(id_after)  # Cancela qualquer chamada ativa
        id_after = None

# Criando Labels --------------------------
Label(app, text='Cronômetro', font=('Arial', 10, 'bold'), bg='black', fg='white').place(x=20, y=5)

label_tempo = Label(app, text="00:00:00", font=('Times', 50, 'bold'), bg='black', fg='#30bff2')
label_tempo.place(x=20, y=30)

# Botões -----------------------------------
Button(app, command=start, text='Iniciar', width=10, height=2, bg='white', fg='black', font=('Ivy', 8, 'bold'), relief='raised', overrelief='ridge').place(x=20, y=120)
Button(app, command=pausar, text='Pausar', width=10, height=2, bg='white', fg='black', font=('Ivy', 8, 'bold'), relief='raised', overrelief='ridge').place(x=112, y=120)
Button(app, command=reiniciar, text='Reiniciar', width=10, height=2, bg='white', fg='black', font=('Ivy', 8, 'bold'), relief='raised', overrelief='ridge').place(x=206, y=120)

# Mantendo o programa em execução
app.mainloop()