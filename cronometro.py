from tkinter import *
import tkinter

# Configurando o app ---------------------
app = Tk()
app.title('')
app.geometry('300x180')
app.config(bg='black')
app.resizable(width=FALSE, height=FALSE)

# Definindo variáveis globais -----------
global cont
global tempo
global rodar
global limitador

#Funções --------------------------------
    #Declaração de variáveis
tempo = '00:00:00'
rodar = False
cont = 1
limitador = 5

    #Função para dar início a contagem regressiva -------
def start():
    global rodar
    rodar = True
    iniciar()

    #Função para a contagem regressiva ----------
def iniciar():
    global cont
    global tempo
    global limitador
    s = 0
    if rodar:
       
        label_tempo['font'] = ('Times', 50, 'bold')

        temporario = str(tempo)
        h, m, s = map(int, temporario.split(":"))
        h = int(h)
        m = int(m)
        s = int(cont)
        cont = 1
        if cont == 0:
                m += 1 
        #Contando os segundos
        if (s >= limitador):
            cont = -1
            
        #Contando os minutos
        if (m > limitador):
            m = 0
            h += 1

        s = str(0) + str(s)
        m = str(0) + str(m)
        h = str(0) + str(h)
        
        #Atualizando os valores atuais
        temporario = str(h[-2:]) + ":" + str(m[-2:]) + ":" + str(s[-2:])
        label_tempo['text'] = temporario
        tempo = temporario
                               
        label_tempo.after(1000, iniciar)
        cont += 1  

    #Função para pausar a contagem
def pausar():
    global rodar
    rodar = False

    #Função para reiniciar
def reiniciar():
    global tempo
    global cont
    cont = 1
    tempo = '00:00:00'
    label_tempo['text'] = tempo
    pausar()
    
#Criando Labels --------------------------
label_nome = Label(app, text='Cronômetro', font=('Arial', 10, 'bold'), bg='black', fg='white')
label_nome.place(x=20, y=5)

label_tempo = Label(app, text=tempo, font=('Times', 50, 'bold'), bg='black', fg='#30bff2')
label_tempo.place(x=20, y=30)

#Botões -----------------------------------
botao_iniciar = Button(app, command=start, text='Iniciar', width=10, height=2, bg='white', fg='black', font=('Ivy', 8, 'bold'), relief='raised', overrelief='ridge')
botao_iniciar.place(x=20, y=120)

botao_pausar = Button(app, command=pausar, text='Pausar', width=10, height=2, bg='white', fg='black', font=('Ivy', 8, 'bold'), relief='raised', overrelief='ridge')
botao_pausar.place(x=112, y=120)

botao_reiniciar = Button(app, command=reiniciar, text='Reiniciar', width=10, height=2, bg='white', fg='black', font=('Ivy', 8, 'bold'), relief='raised', overrelief='ridge')
botao_reiniciar.place(x=206, y=120)

#Código para manter o programa na tela
app.mainloop()