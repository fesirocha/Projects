from tkinter import *

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
    if not rodar:
        rodar = True
        iniciar()

    #Função para a contagem regressiva ----------
def iniciar():
    global cont, tempo, limitador, rodar
    #s = 1
    
    if rodar:
        
        temporario = str(tempo)
        h, m, s = map(int, temporario.split(":"))
        #h = int(h)
        #m = int(m)
        #s = int(cont)
        s = cont  
        
        if cont == 0:
            m += 1 
        #Limitando os segundos
        if (s >= limitador):
            cont = -1
            
        #Contando os minutos
        if (m > limitador):
            m = 0
            h += 1

        #Atualizando os valores atuais     
        s = str(0) + str(s)
        m = str(0) + str(m)
        h = str(0) + str(h)
        
        
        temporario = (h[-2:]) + ":" + (m[-2:]) + ":" + (s[-2:])
        label_tempo['text'] = temporario
        tempo = temporario
        cont += 1                       
        label_tempo.after(1000, iniciar)   

    #Função para pausar a contagem
def pausar():
    global rodar
    rodar = False

    #Função para reiniciar
def reiniciar():
    global tempo, cont, rodar
    rodar = False
    cont = 1
    tempo = '00:00:00'
    label_tempo['text'] = tempo
    
    
#Criando Labels --------------------------
Label(app, text='Cronômetro', font=('Arial', 10, 'bold'), bg='black', fg='white').place(x=20, y=5)

label_tempo = Label(app, text=tempo, font=('Times', 50, 'bold'), bg='black', fg='#30bff2')
label_tempo.place(x=20, y=30)

#Botões -----------------------------------
Button(app, command=start, text='Iniciar', width=10, height=2, bg='white', fg='black', font=('Ivy', 8, 'bold'), relief='raised', overrelief='ridge').place(x=20, y=120)
Button(app, command=pausar, text='Pausar', width=10, height=2, bg='white', fg='black', font=('Ivy', 8, 'bold'), relief='raised', overrelief='ridge').place(x=112, y=120)
Button(app, command=reiniciar, text='Reiniciar', width=10, height=2, bg='white', fg='black', font=('Ivy', 8, 'bold'), relief='raised', overrelief='ridge').place(x=206, y=120)

#Manter programa em execução
app.mainloop()