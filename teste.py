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
segundos = 0  # Usado para contar o tempo corretamente

# Função para iniciar o cronômetro --------
def iniciar():
    global segundos, rodar

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
        label_tempo.after(1000, iniciar)

# Função para dar início ao cronômetro ----
def start():
    global rodar
    if not rodar:
        rodar = True
        iniciar()

# Função para pausar ---------------------
def pausar():
    global rodar
    rodar = False

# Função para reiniciar ------------------
def reiniciar():
    global segundos, rodar
    rodar = False
    segundos = 0
    label_tempo.config(text="00:00:00")

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