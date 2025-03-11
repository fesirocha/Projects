from tkinter import *

#Configurando app ---------------------
app = Tk()
app.title('')
app.geometry('300x180')
app.resizable(width=False, height=False)
app.config(bg='black')

#Declarando Variáveis Globais ----------
rodar = False
segundos = 0

def start():
    global rodar
    if not rodar:
        rodar = True
        iniciar()

def iniciar ():
    global segundos, rodar
    if rodar:
        #Convertendo segs para horas, minutos e segundos
        h = segundos // 3600
        m = (segundos%3600)//60
        s = segundos % 60

        #Alterando texto
        texto_formatado = f'{h:02}:{m:02}:{s:02}'
        label_tempo['text'] = texto_formatado

        #Incrementando texto
        segundos += 1
        label_tempo.after(1000, iniciar)

def pausar():
    global rodar
    rodar = False

def reiniciar():
    global rodar, segundos
    rodar = False
    label_tempo['text'] = '00:00:00'
    segundos = 0

#Labels and Buttons
Label(app, text='Cronômetro', font=('Arial', 10, 'bold'), bg='black', fg='white').place(x=10, y=10)

label_tempo = Label(app, text='00:00:00', font=('Times', 50, 'bold'), bg='black', fg='red')
label_tempo.place(x= 20, y=30)

Button(app, text='Iniciar', command=start, width=10, height=2, font=('Ivy', 10, 'bold'), relief='raised', overrelief='groove').place(x=10, y=110)
Button(app, text='Pausar', command=pausar, width=10, height=2, font=('Ivy', 10, 'bold'), relief='raised', overrelief='groove').place(x=105, y=110)
Button(app, text='Reiniciar', command=reiniciar, width=10, height=2, font=('Ivy', 10, 'bold'), relief='raised', overrelief='groove').place(x=200, y=110)

#Para rodar o app
app.mainloop()