from dataclasses import replace
from tkinter import *
from tkinter import ttk
import os
import math

os.system('cls')

answer = ''
all_values = ''
all_values2 = ''
all_values3 = ''
a = ''
a2 = ''

#CORES
cyan = '#04bfbf'
black = '#292928'
light_grey = '#D3D3D3'
dark = '#1c1b1b'
grey = '#292928'


#-------------------------------------------- JANELA CONVERSOR ----------------------------------------------

#CRIANDO FUNÇÃO COMO COMANDOS PARA OS BOTÕES CONVERTER E FÓRMULA
    #BOTÃO CONVERTER
def convertbtn():
    window.withdraw()

    global all_values2
    all_values2 = ''

    windowConvert = Toplevel()
    windowConvert.title('Conversor')
    windowConvert.iconbitmap('icon.ico')
    windowConvert.config(bg=black)
    windowConvert.geometry('479x539')
    windowConvert.resizable(False, False)


    #CRIANDO FUNÇÃO PARA VOLTAR A JANELA
    def back():
        windowConvert.destroy()
        window.deiconify()



    #CRIANDO FUNÇÃO PARA RECEBER OS CARACTERES DAS EXPRESSÕES
    def show2(event):
        text_value3.set('')

        global all_values2
        all_values2 = all_values2 + str(event)
        
        #PASSANDO VALOR PARA A TELA
        text_value2.set(all_values2)


    #FRAMES
    frame_convert = Frame(windowConvert, width=479, height=100, bg=black)
    frame_convert.grid(row=0, column=0)

    frame_convert2 = Frame(windowConvert, width=479, height=100, bg=black)
    frame_convert2.grid(row=1, column=0)

    frame = Frame(windowConvert, width=479, height=339, bg=dark)
    frame.grid(row=2, column=0)


    #CRIANDO LABEL
    text_value2 = StringVar()
    text_value3 = StringVar()

    display2 = Label(frame_convert, textvariable=text_value2, width=16, height=2, padx=28, relief=FLAT, anchor='e', justify=RIGHT,
                    bg=black, fg='white', font='Ivy 35')
    display2.place(x=0, y=0)


    display2 = Label(frame_convert2, textvariable=text_value3, width=16, height=2, padx=28, relief=FLAT, anchor='e', justify=RIGHT,
                    bg=black, fg='white', font='Ivy 35')
    display2.place(x=0, y=0)


    #CRIANDO CAIXA DE OPÇÕES
    def comboclick(event):
        options_C = ['Quilômetro', 'Metro', 'Centímetro', 'Milímetro']
        options_M = ['Tonelada', 'Quilograma', 'Grama', 'Miligrama']
        options_T = ['Grau Celsius', 'Grau Fahreinheit', 'Kelvin']
        options_Time = ['Segundo', 'Minuto', 'Hora']
        options_V = ['Metro cúbico', 'Litro', 'Mililitro']


        if myCombo.get() == 'Comprimento':
            def value(event):
                global a
                global a2

                if myCombo_C.get() == 'Quilômetro':
                    a = 'Quilômetro'
                if myCombo_C.get() == 'Metro':
                    a = 'Metro'
                if myCombo_C.get() == 'Centímetro':
                    a = 'Centímetro'
                if myCombo_C.get() == 'Milímetro':
                    a = 'Milímetro'


                if myCombo_C2.get() == 'Quilômetro':
                    a2 = 'Quilômetro'
                if myCombo_C2.get() == 'Metro':
                    a2 = 'Metro'
                if myCombo_C2.get() == 'Centímetro':
                    a2 = 'Centímetro'
                if myCombo_C2.get() == 'Milímetro':
                    a2 = 'Milímetro'

            
            myCombo_C = ttk.Combobox(frame_convert, value=options_C, width=16)
            myCombo_C.current(0)
            myCombo_C.bind("<<ComboboxSelected>>", value)
            myCombo_C.place(x=0, y=0)

            myCombo_C2 = ttk.Combobox(frame_convert2, value=options_C, width=16)
            myCombo_C2.current(0)
            myCombo_C2.bind("<<ComboboxSelected>>", value)
            myCombo_C2.place(x=0, y=0)      


        if myCombo.get() == 'Massa':
            def value2(event):
                global a
                global a2

                if myCombo_M.get() == 'Tonelada':
                    a = 'Tonelada'
                if myCombo_M.get() == 'Quilograma':
                    a = 'Quilograma'
                if myCombo_M.get() == 'Grama':
                    a = 'Grama'
                if myCombo_M.get() == 'Miligrama':
                    a = 'Miligrama'

                    
                if myCombo_M2.get() == 'Tonelada':
                    a2 = 'Tonelada'
                if myCombo_M2.get() == 'Quilograma':
                    a2 = 'Quilograma'
                if myCombo_M2.get() == 'Grama':
                    a2 = 'Grama'
                if myCombo_M2.get() == 'Miligrama':
                    a2 = 'Miligrama'


            myCombo_M = ttk.Combobox(frame_convert, value=options_M, width=16)
            myCombo_M.current(0)
            myCombo_M.bind("<<ComboboxSelected>>", value2)
            myCombo_M.place(x=0, y=0)

            myCombo_M2 = ttk.Combobox(frame_convert2, value=options_M, width=16)
            myCombo_M2.current(0)
            myCombo_M2.bind("<<ComboboxSelected>>", value2)
            myCombo_M2.place(x=0, y=0)

        
        if myCombo.get() == 'Temperatura':
            def value3(event):
                global a
                global a2

                if myCombo_T.get() == 'Grau Celsius':
                    a = 'Grau Celsius'
                if myCombo_T.get() == 'Grau Fahreinheit':
                    a = 'Grau Fahreinheit'
                if myCombo_T.get() == 'Kelvin':
                    a = 'Kelvin'


                if myCombo_T2.get() == 'Grau Celsius':
                    a2 = 'Grau Celsius'
                if myCombo_T2.get() == 'Grau Fahreinheit':
                    a2 = 'Grau Fahreinheit'
                if myCombo_T2.get() == 'Kelvin':
                    a2 = 'Kelvin'


            myCombo_T = ttk.Combobox(frame_convert, value=options_T, width=16)
            myCombo_T.current(0)
            myCombo_T.bind("<<ComboboxSelected>>", value3)
            myCombo_T.place(x=0, y=0)
            
            myCombo_T2 = ttk.Combobox(frame_convert2, value=options_T, width=16)
            myCombo_T2.current(0)
            myCombo_T2.bind("<<ComboboxSelected>>", value3)
            myCombo_T2.place(x=0, y=0)


        if myCombo.get() == 'Tempo':
            def value4(event):
                global a
                global a2

                if myCombo_Time.get() == 'Segundo':
                    a = 'Segundo'
                if myCombo_Time.get() == 'Minuto':
                    a = 'Minuto'
                if myCombo_Time.get() == 'Hora':
                    a = 'Hora'


                if myCombo_Time2.get() == 'Segundo':
                    a2 = 'Segundo'
                if myCombo_Time2.get() == 'Minuto':
                    a2 = 'Minuto'
                if myCombo_Time2.get() == 'Hora':
                    a2 = 'Hora'


            myCombo_Time = ttk.Combobox(frame_convert, value=options_Time, width=16)
            myCombo_Time.current(0)
            myCombo_Time.bind("<<ComboboxSelected>>", value4)
            myCombo_Time.place(x=0, y=0)

            myCombo_Time2 = ttk.Combobox(frame_convert2, value=options_Time, width=16)
            myCombo_Time2.current(0)
            myCombo_Time2.bind("<<ComboboxSelected>>", value4)
            myCombo_Time2.place(x=0, y=0)


        if myCombo.get() == 'Volume':
            def value5(event):
                global a
                global a2

                if myCombo_V.get() == 'Metro cúbico':
                    a = 'Metro cúbico'
                if myCombo_V.get() == 'Litro':
                    a = 'Litro'
                if myCombo_V.get() == 'Mililitro':
                    a = 'Mililitro'


                if myCombo_V2.get() == 'Metro cúbico':
                    a2 = 'Metro cúbico'
                if myCombo_V2.get() == 'Litro':
                    a2 = 'Litro'
                if myCombo_V2.get() == 'Mililitro':
                    a2 = 'Mililitro'


            myCombo_V = ttk.Combobox(frame_convert, value=options_V, width=16)
            myCombo_V.current(0)
            myCombo_V.bind("<<ComboboxSelected>>", value5)
            myCombo_V.place(x=0, y=0)

            myCombo_V2 = ttk.Combobox(frame_convert2, value=options_V, width=16)
            myCombo_V2.current(0)
            myCombo_V2.bind("<<ComboboxSelected>>", value5)
            myCombo_V2.place(x=0, y=0)


    options = ['Comprimento', 'Massa', 'Temperatura', 'Tempo', 'Volume']
    options_C = ['Quilômetro', 'Metro', 'Centímetro', 'Milímetro']


    myCombo = ttk.Combobox(frame, value=options, width=76)
    myCombo.bind("<<ComboboxSelected>>", comboclick)
    myCombo.current(0)
    myCombo.place(x=0, y=0)
    
    def valueMain(event):
        global a
        global a2

        if myCombo_C.get() == 'Quilômetro':
            a = 'Quilômetro'
        if myCombo_C.get() == 'Metro':
            a = 'Metro'
        if myCombo_C.get() == 'Centímetro':
            a = 'Centímetro'
        if myCombo_C.get() == 'Milímetro':
            a = 'Milímetro'


        if myCombo_C2.get() == 'Quilômetro':
            a2 = 'Quilômetro'
        if myCombo_C2.get() == 'Metro':
            a2 = 'Metro'
        if myCombo_C2.get() == 'Centímetro':
            a2 = 'Centímetro'
        if myCombo_C2.get() == 'Milímetro':
            a2 = 'Milímetro'


    myCombo_C = ttk.Combobox(frame_convert, value=options_C, width=16)
    myCombo_C.current(0)
    myCombo_C.bind("<<ComboboxSelected>>", valueMain)
    myCombo_C.place(x=0, y=0)

    myCombo_C2 = ttk.Combobox(frame_convert2, value=options_C, width=16)
    myCombo_C2.current(0)
    myCombo_C2.bind("<<ComboboxSelected>>", valueMain)
    myCombo_C2.place(x=0, y=0)



    #CRIANDO FUNCÃO PARA BOTÃOCONVERTER
    def convert():
        global all_values2
        global a
        global a2


        #COMPRIMENTO
        try:
            if a == 'Quilômetro':
                if a2 == 'Metro':
                    result2 = float(all_values2) * 1000
                    text_value3.set(result2)
                if a2 == 'Centímetro':
                    result2 = float(all_values2) * 100000
                    text_value3.set(result2)
                if a2 == 'Milímetro':
                    result2 = float(all_values2) * 1e+6
                    text_value3.set(result2)

            if a == 'Metro':
                if a2 == 'Quilômetro':
                    result2 = float(all_values2) / 1000
                    text_value3.set(result2)
                if a2 == 'Centímetro':
                    result2 = float(all_values2) * 100
                    text_value3.set(result2)
                if a2 == 'Milímetro':
                    result2 = float(all_values2) * 1000
                    text_value3.set(result2)

            if a == 'Centímetro':
                if a2 == 'Quilômetro':
                    result2 = float(all_values2) / 100000
                    text_value3.set(result2)
                if a2 == 'Metro':
                    result2 = float(all_values2) / 100
                    text_value3.set(result2)
                if a2 == 'Milímetro':
                    result2 = float(all_values2) * 10
                    text_value3.set(result2)

            if a == 'Milímetro':
                if a2 == 'Quilômetro':
                    result2 = float(all_values2) / 1e+6
                    text_value3.set(result2)
                if a2 == 'Metro':
                    result2 = float(all_values2) / 1000
                    text_value3.set(result2)
                if a2 == 'Centímetro':
                    result2 = float(all_values2) / 10
                    text_value3.set(result2)
        except:
            text_value3.set('Error')


        #MASSA
        try:
            if a == 'Tonelada':
                if a2 == 'Quilograma':
                    result2 = float(all_values2) * 1000
                    text_value3.set(result2)
                if a2 == 'Grama':
                    result2 = float(all_values2) * 1e+6
                    text_value3.set(result2)
                if a2 == 'Miligrama':
                    result2 = float(all_values2) * 1e+9
                    text_value3.set(result2)

            if a == 'Quilograma':
                if a2 == 'Tonelada':
                    result2 = float(all_values2) / 1000
                    text_value3.set(result2)
                if a2 == 'Grama':
                    result2 = float(all_values2) * 1000
                    text_value3.set(result2)
                if a2 == 'Miligrama':
                    result2 = float(all_values2) * 1e+6
                    text_value3.set(result2)

            if a == 'Grama':
                if a2 == 'Tonelada':
                    result2 = float(all_values2) / 1e+6
                    text_value3.set(result2)
                if a2 == 'Quilograma':
                    result2 = float(all_values2) / 1000
                    text_value3.set(result2)
                if a2 == 'Miligrama':
                    result2 = float(all_values2) * 1000
                    text_value3.set(result2)

            if a == 'Miligrama':
                if a2 == 'Tonelada':
                    result2 = float(all_values2) / 1e+9
                    text_value3.set(result2)
                if a2 == 'Quilograma':
                    result2 = float(all_values2) / 1e+6
                    text_value3.set(result2)
                if a2 == 'Grama':
                    result2 = float(all_values2) / 1000
                    text_value3.set(result2)
        except:
            text_value3.set('Error')


        #TEMPERATURA
        try:
            if a == 'Grau Celsius':
                if a2 == 'Grau Fahreinheit':
                    result2 = (float(all_values2) * 9/5) + 32
                    text_value3.set(result2)
                if a2 == 'Kelvin':
                    result2 = float(all_values2) + 273.15
                    text_value3.set(result2)

            if a == 'Grau Fahreinheit':
                if a2 == 'Grau Celsius':
                    result2 = (float(all_values2) - 32) * 5/9 
                    text_value3.set(round(result2, 4)) # 4 casas depois da vírgula
                if a2 == 'Kelvin':
                    result2 = (float(all_values2) - 32) * 5/9 + 273.15
                    text_value3.set(round(result2, 3)) # 3 casas depois da vírgula

            if a == 'Kelvin':
                if a2 == 'Grau Celsius':
                    result2 = float(all_values2) - 273.15
                    text_value3.set(result2)
                if a2 == 'Grau Fahreinheit':
                    result2 = (float(all_values2) - 273.15) * 9/5 + 32
                    text_value3.set(result2)
        except:
            text_value3.set('Error')


        #TEMPO
        try:
            if a == 'Segundo':
                if a2 == 'Minuto':
                    result2 = float(all_values2) / 60
                    text_value3.set(round(result2, 7)) # 7 casas depois da vírgula
                if a2 == 'Hora':
                    result2 = float(all_values2) / 3600
                    text_value3.set(round(result2, 9)) # 9 casas depois da vírgula

            if a == 'Minuto':
                if a2 == 'Segundo':
                    result2 = float(all_values2) * 60
                    text_value3.set(result2)
                if a2 == 'Hora':
                    result2 = float(all_values2) / 60
                    text_value3.set(round(result2, 7)) # 7 casas depois da vírgula

            if a == 'Hora':
                if a2 == 'Segundo':
                    result2 = float(all_values2) * 3600
                    text_value3.set(result2)
                if a2 == 'Minuto':
                    result2 = float(all_values2) * 60
                    text_value3.set(result2)
        except:
            text_value3.set('Error')

        
        #VOLUME
        try:
            if a == 'Metro cúbico':
                if a2 == 'Litro':
                    result2 = float(all_values2) * 1000
                    text_value3.set(result2)
                if a2 == 'Mililitro':
                    result2 = float(all_values2) * 1e+6
                    text_value3.set(result2)

            if a == 'Litro':
                if a2 == 'Metro cúbico':
                    result2 = float(all_values2) / 1000
                    text_value3.set(result2)
                if a2 == 'Mililitro':
                    result2 = float(all_values2) * 1000
                    text_value3.set(result2)

            if a == 'Mililitro':
                if a2 == 'Metro cúbico':
                    result2 = float(all_values2) / 1e+6
                    text_value3.set(result2)
                if a2 == 'Litro':
                    result2 = float(all_values2) / 1000
                    text_value3.set(result2)
        except:
            text_value3.set('Error')


        all_values2 = ''
        



    #BOTÕES
    b_1 = Button(frame, text='1', width=15, height=3, bg=dark, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= lambda: show2('1'), fg='white')
    b_1.place(x=0, y=164)

    b_2 = Button(frame, text='2', width=15, height=3, bg=dark, font='Ivy 13 bold', relief=RAISED, 
                overrelief=RIDGE, command= lambda: show2('2'), fg='white')
    b_2.place(x=160, y=164)

    b_3 = Button(frame, text='3', width=15, height=3, bg=dark, font='Ivy 13 bold', relief=RAISED, 
                overrelief=RIDGE, command= lambda: show2('3'), fg='white')
    b_3.place(x=320, y=164)


    b_4 = Button(frame, text='4', width=15, height=3, bg=dark, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= lambda: show2('4'), fg='white')
    b_4.place(x=0, y=93)

    b_5 = Button(frame, text='5', width=15, height=3, bg=dark, font='Ivy 13 bold', relief=RAISED, 
                overrelief=RIDGE, command= lambda: show2('5'), fg='white')
    b_5.place(x=160, y=93)

    b_6 = Button(frame, text='6', width=15, height=3, bg=dark, font='Ivy 13 bold', relief=RAISED, 
                overrelief=RIDGE, command= lambda: show2('6'), fg='white')
    b_6.place(x=320, y=93)


    b_7 = Button(frame, text='7', width=15, height=3, bg=dark, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= lambda: show2('7'), fg='white')
    b_7.place(x=0, y=22)

    b_8 = Button(frame, text='8', width=15, height=3, bg=dark, font='Ivy 13 bold', relief=RAISED, 
                overrelief=RIDGE, command= lambda: show2('8'), fg='white')
    b_8.place(x=160, y=22)

    b_9 = Button(frame, text='9', width=15, height=3, bg=dark, font='Ivy 13 bold', relief=RAISED, 
                overrelief=RIDGE, command= lambda: show2('9'), fg='white')
    b_9.place(x=320, y=22)


    b_0 = Button(frame, text='0', width=31, height=3, bg=dark, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= lambda: show2('0'), fg='white')
    b_0.place(x=0, y=235)

    b_Vir = Button(frame, text=',', width=15, height=3, bg=dark, font='Ivy 13 bold', relief=RAISED, 
                overrelief=RIDGE, command= lambda: show2('.'), fg='white')
    b_Vir.place(x=320, y=235)

    b_Ig = Button(frame, text='Converter', width=52, height=1, bg=cyan, font='Ivy 13', relief=RAISED, 
                overrelief=RIDGE, command=convert)
    b_Ig.place(x=1, y=306)

    b_back = Button(frame_convert, text='↩', width=1, height=1, bg=black, font='Ivy 25 bold', relief=RAISED, 
                overrelief=RIDGE, command=back, bd=0, fg='white', cursor='hand2')
    b_back.place(x=458, y=-18)



    windowConvert.mainloop()


#------------------------------------------- JANELA FÓRMULAS --------------------------------------------------

#BOTÃO FÓRMULA
def formula():
    window.withdraw()

    windowF = Toplevel()
    windowF.title('Fórmulas')
    windowF.iconbitmap('icon.ico')
    windowF.config(bg=black)
    windowF.geometry('462x424')
    windowF.resizable(False, False)

    #FRAMES
    frame = Frame(windowF, width=479, height=200, bg=black)
    frame.grid(row=0, column=0)

    frameF = Frame(windowF, width=479, height=339, bg='blue')
    frameF.grid(row=2, column=0)


    #CRIANDO FUNÇÃO PARA VOLTAR A JANELA
    def back2():
        windowF.destroy()
        window.deiconify()



    #CRIANDO FUNÇÃO PARA ARMEZENAR VALORES DO BOTÕES
    def take(event):
        global all_values3
        global myLabel, myLabel2, myLabel3, myLabel4, myLabel5, myLabel6
        global fra, fra2

        myLabel.destroy()
        myLabel2.destroy()
        myLabel3.destroy()
        myLabel4.destroy()
        myLabel5.destroy()
        myLabel6.destroy()
        fra.destroy()
        fra2.destroy()

        all_values3 = event
        text_value4.set(event)

    #CRIANDO FUNÇÃO PARA MOSTRAR AS FÓRMULAS NA TELA
    def showit():
        global all_values3
        global myLabel, myLabel2, myLabel3, myLabel4, myLabel5, myLabel6
        global fra, fra2

        myLabel = Label(frame, text='', bg=black)
        myLabel.place(x=0, y=0)

        fra = Frame(frame, bg=black)
        fra.place(x=0, y=0)

        if all_values3 == 'ρ':
            text_value4.set('')

            myLabel = Label(frame, text='ρ = m\n      V', font='Ivy 45', bg=black, fg='white')
            myLabel.place(x=295, y=50)

            fra = Frame(frame, bg='white', width=60, height=5)
            fra.place(x=395, y=118)

        if all_values3 == 'e':
            text_value4.set('')

            myLabel = Label(frame, text='2', font='Ivy, 20', bg=black, fg='white')
            myLabel.place(x=435, y=70)

            myLabel2 = Label(frame, text='-0,25.(ΔE)', font='Ivy, 30', bg=black, fg='white')
            myLabel2.place(x=245, y=85)

            myLabel3 = Label(frame, text='e', font='Ivy, 45', bg=black, fg='white')
            myLabel3.place(x=215, y=100)

        if all_values3 == 'A':
            text_value4.set('')

            myLabel = Label(frame, text='-28', font='Ivy, 20', bg=black, fg='white')
            myLabel.place(x=253, y=65)

            myLabel2 = Label(frame, text='A = 2,3.10.|Z1|.|Z2|', font='Ivy, 35', bg=black, fg='white')
            myLabel2.place(x=58, y=95)

        if all_values3 == 'Q':
            text_value4.set('')

            myLabel = Label(frame, text='Q = A . d', font='Ivy 45', bg=black, fg='white')
            myLabel.place(x=200, y=80)

        if all_values3 == 'd':
            text_value4.set('')

            myLabel = Label(frame, text='d = 4r\n      3π', font='Ivy 45', bg=black, fg='white')
            myLabel.place(x=270, y=50)

            fra = Frame(frame, bg='white', width=85, height=4)
            fra.place(x=370, y=118)

        if all_values3 == 'r':
            text_value4.set('')

            myLabel = Label(frame, text='(    )', font='Ivy 55', bg=black, fg='white')
            myLabel.place(x=281, y=75)
            
            myLabel2 = Label(frame, text=' A\n nB', font='Ivy 35', bg=black, fg='white')
            myLabel2.place(x=305, y=65)
            
            myLabel3 = Label(frame, text='1-n', font='Ivy 20', bg=black, fg='white')
            myLabel3.place(x=410, y=73)

            myLabel4 = Label(frame, text='1', font='Ivy 20', bg=black, fg='white')
            myLabel4.place(x=422, y=45)

            myLabel5 = Label(frame, text='r =', font='Ivy 35', bg=black, fg='white')
            myLabel5.place(x=205, y=95)

            myLabel6 = Label(frame, text='o', font='Ivy 20', bg=black, fg='white')
            myLabel6.place(x=218, y=132)

            fra = Frame(frame, bg='white', width=65, height=4)
            fra.place(x=315, y=120)

            fra2 = Frame(frame, bg='white', width=40, height=3)
            fra2.place(x=415, y=77)
        
        if all_values3 == 'σ':
            text_value4.set('')

            myLabel = Label(frame, text='σ = F\n      A', font='Ivy 45', bg=black, fg='white')
            myLabel.place(x=295, y=50)

            fra = Frame(frame, bg='white', width=60, height=4)
            fra.place(x=390, y=118)

        if all_values3 == 'ΔL':
            text_value4.set('')

            myLabel = Label(frame, text='ΔL = Lf - Lo', font='Ivy 45', bg=black, fg='white')
            myLabel.place(x=145, y=80)

        if all_values3 == 'Fs':
            text_value4.set('')

            myLabel2 = Label(frame, text='     ult\n\n       adm', font='Ivy 20', bg=black, fg='white')
            myLabel2.place(x=330, y=85)

            myLabel = Label(frame, text='Fs = σ\n        σ', font='Ivy 45', bg=black, fg='white')
            myLabel.place(x=210, y=50)

            fra = Frame(frame, bg='white', width=120, height=4)
            fra.place(x=330, y=123)

        if all_values3 == 'ϵ':
            text_value4.set('')

            myLabel = Label(frame, text='ϵ = ΔL\n      Lo', font='Ivy 45', bg=black, fg='white')
            myLabel.place(x=280, y=50)

            fra = Frame(frame, bg='white', width=70, height=4)
            fra.place(x=380, y=118)

        if all_values3 == 'Ao':
            text_value4.set('')

            myLabel = Label(frame, text='A = π . d²\n       4', font='Ivy 45', bg=black, fg='white')
            myLabel.place(x=190, y=50)

            fra = Frame(frame, bg='white', width=150, height=4)
            fra.place(x=300, y=123)

        all_values3 = ''

    #LABEL
    text_value4 = StringVar()

    display = Label(frame, textvariable=text_value4, width=16, height=3, padx=0, relief=FLAT, anchor='e', 
                    justify=RIGHT,
                    bg=black, fg='white', font='Ivy 55')
    display.place(x=-235, y=-20)


    #BOTÕES
    b_1 = Button(frameF, text='σ', width=9, height=1, bg=dark, font='Ivy 20', relief=RAISED, 
            overrelief=RIDGE, fg='white', command= lambda: take('σ'))
    b_1.place(x=0, y=112)

    b_2 = Button(frameF, text='ΔL', width=9, height=1, bg=dark, font='Ivy 20', relief=RAISED, 
                overrelief=RIDGE, fg='white', command= lambda: take('ΔL'))
    b_2.place(x=154, y=112)

    b_3 = Button(frameF, text='Fs', width=9, height=1, bg=dark, font='Ivy 20', relief=RAISED, 
                overrelief=RIDGE, fg='white', command= lambda: take('Fs'))
    b_3.place(x=308, y=112)


    b_4 = Button(frameF, text='Q', width=9, height=1, bg=dark, font='Ivy 20', 
                 relief=RAISED, 
                 overrelief=RIDGE, fg='white', command=lambda: take('Q'))
    b_4.place(x=0, y=56)

    b_5 = Button(frameF, text='d', width=9, height=1, bg=dark, font='Ivy 20', relief=RAISED, 
                overrelief=RIDGE, fg='white', command=lambda: take('d'))
    b_5.place(x=154, y=56)

    b_6 = Button(frameF, text='r', width=9, height=1, bg=dark, font='Ivy 20', 
                relief=RAISED, 
                overrelief=RIDGE, fg='white', command=lambda: take('r'))
    b_6.place(x=308, y=56)


    b_7 = Button(frameF, text='ρ', width=9, height=1, bg=dark, font='Ivy 20', relief=RAISED, 
            overrelief=RIDGE, fg='white', command=lambda: take('ρ'))
    b_7.place(x=0, y=0)

    b_8 = Button(frameF, text='e', width=9, height=1, bg=dark, font='Ivy 20', 
                relief=RAISED, 
                overrelief=RIDGE, fg='white', command=lambda: take('e'))
    b_8.place(x=154, y=0)

    b_9 = Button(frameF, text='A', width=9, height=1, bg=dark, font='Ivy 20', 
                relief=RAISED, 
                overrelief=RIDGE, fg='white', command=lambda: take('A'))
    b_9.place(x=308, y=0)


    b_0 = Button(frameF, text='ϵ', width=9, height=1, bg=dark, font='Ivy 20', relief=RAISED, 
            overrelief=RIDGE, fg='white', command= lambda: take('ϵ'))
    b_0.place(x=0, y=168)

    b = Button(frameF, text='Ao', width=9, height=1, bg=dark, font='Ivy 20', relief=RAISED, 
            overrelief=RIDGE, fg='white', command= lambda: take('Ao'))
    b.place(x=154, y=168)

    b_Vir = Button(frameF, text='=', width=9, height=1, bg=cyan, font='Ivy 20', relief=RAISED, 
                overrelief=RIDGE, command=showit)
    b_Vir.place(x=308, y=168)

    b_back = Button(frame, text='↩', width=1, height=1, bg=black, font='Ivy 25 bold', relief=RAISED, 
                overrelief=RIDGE, command=back2, bd=0, fg='white', cursor='hand2')
    b_back.place(x=435, y=-10)



    windowF.mainloop()

#------------------------------------------- JANELA PRINCIPAL -------------------------------------------------

#CRIANDO FUNÇÃO PARA RECEBER OS CARACTERES DAS EXPRESSÕES
def show(event):
    global all_values
    all_values = all_values + str(event)
    
    #PASSANDO VALOR PARA A TELA
    text_value.set(all_values)


#CRIANDO FUNÇÃO PARA CALCULAR AS EXPRESSÕES
def calculate():
    global all_values
    global answer


    mod = ['math.sqrt', 'math.e', 'math.pi']

    for i in mod:
        if i == 'math.sqrt':
            all_values = all_values.replace('√', i)

        if i == 'math.e':
            all_values = all_values.replace('e', i)

        if i == 'math.pi':
            all_values = all_values.replace('π', i)


    try:
        result = eval(all_values)
        answer = result

        text_value.set(str(result))
    except:
        text_value.set('Error')

    all_values = ''


#CRIANDO FUNÇÃO PARA LIMPAR A TELA
def clear():
    global all_values
    all_values = ''
    text_value.set('')


#CRIANDO FUNÇÃO PARA OS BOTÕES ENG, EXP E ANS
    #ANS
def ans():
    global all_values
    global answer

    show(answer)



#CRIANDO E CONFIGURANDO JANELA
window = Tk()
window.title('Calculadora Científica')
window.iconbitmap('icon.ico')
window.config(bg='black')
window.geometry('479x514')
window.resizable(False, False)

#CRIANDO FRAME PARA PERSONALIZAR A JANELA
frame = Frame(window, width=479, height=150, bg='black')
frame.grid(row=0, column=0)

frame_scientific = Frame(window, width=479, height=104, bg='blue')
frame_scientific.grid(row=1, column=0)

frame2 = Frame(window, width=479, height=285, bg='green')
frame2.grid(row=2, column=0)


#CRIANDO LABEL
text_value = StringVar()

display = Label(frame, textvariable=text_value, width=16, height=3, padx=40, relief=FLAT, anchor='e', justify=RIGHT,
                bg=black, fg='white', font='Ivy 35')
display.place(x=0, y=0)


#CRIANDO BOTÕES
    #FILA 1
b_C = Button(frame2, text='C', width=23, height=2, bg=grey, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= clear, fg='white')
b_C.place(x=0, y=0)

b_R = Button(frame2, text='%', width=11, height=2, bg=grey, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= lambda: show('%'), fg='white')
b_R.place(x=240, y=0)

b_Div = Button(frame2, text='÷', width=11, height=2, bg=grey, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= lambda: show('/'), fg='white')
b_Div.place(x=360, y=0)



    #FILA 2
b_7 = Button(frame2, text='7', width=11, height=2, bg=dark, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= lambda: show('7'), fg='white')
b_7.place(x=0, y=52)

b_8 = Button(frame2, text='8', width=11, height=2, bg=dark, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= lambda: show('8'), fg='white')
b_8.place(x=120, y=52)

b_9 = Button(frame2, text='9', width=11, height=2, bg=dark, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= lambda: show('9'), fg='white')
b_9.place(x=240, y=52)

b_Mult = Button(frame2, text='x', width=11, height=2, bg=grey, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= lambda: show('*'), fg='white')
b_Mult.place(x=360, y=52)



    #FILA 3
b_4 = Button(frame2, text='4', width=11, height=2, bg=dark, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= lambda: show('4'), fg='white')
b_4.place(x=0, y=104)

b_5 = Button(frame2, text='5', width=11, height=2, bg=dark, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= lambda: show('5'), fg='white')
b_5.place(x=120, y=104)

b_6 = Button(frame2, text='6', width=11, height=2, bg=dark, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= lambda: show('6'), fg='white')
b_6.place(x=240, y=104)

b_Sub = Button(frame2, text='-', width=11, height=2, bg=grey, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= lambda: show('-'), fg='white')
b_Sub.place(x=360, y=104)



    #FILA 4
b_1 = Button(frame2, text='1', width=11, height=2, bg=dark, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= lambda: show('1'), fg='white')
b_1.place(x=0, y=156)

b_2 = Button(frame2, text='2', width=11, height=2, bg=dark, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= lambda: show('2'), fg='white')
b_2.place(x=120, y=156)

b_3 = Button(frame2, text='3', width=11, height=2, bg=dark, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= lambda: show('3'), fg='white')
b_3.place(x=240, y=156)

b_Soma = Button(frame2, text='+', width=11, height=2, bg=grey, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= lambda: show('+'), fg='white')
b_Soma.place(x=360, y=156)



    #FILA 5
b_0 = Button(frame2, text='0', width=23, height=2, bg=dark, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= lambda: show('0'), fg='white')
b_0.place(x=0, y=208)

b_Vir = Button(frame2, text=',', width=11, height=2, bg=dark, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= lambda: show('.'), fg='white')
b_Vir.place(x=240, y=208)

b_Ig = Button(frame2, text='=', width=11, height=2, bg=cyan, font='Ivy 13 bold', relief=RAISED, 
            overrelief=RIDGE, command= calculate)
b_Ig.place(x=360, y=208)



    #PARTE CIENTÍFICA
        #FILA 1
b_exponencial = Button(frame_scientific, text='x^', width=11, height=2, bg=dark, font='Ivy 13 bold',
                        relief=RAISED, overrelief=RIDGE, command= lambda: show('**('), fg='white')
b_exponencial.place(x=0, y=0)

b_e = Button(frame_scientific, text='e^', width=11, height=2, bg=dark, font='Ivy 13 bold',
                        relief=RAISED, overrelief=RIDGE, fg='white', command= lambda: show('e**('))
b_e.place(x=120, y=0)

b_e = Button(frame_scientific, text='(', width=11, height=2, bg=dark, font='Ivy 13 bold',
                        relief=RAISED, overrelief=RIDGE, fg='white', command= lambda: show('('))
b_e.place(x=240, y=0)
b_e = Button(frame_scientific, text=')', width=11, height=2, bg=dark, font='Ivy 13 bold',
                        relief=RAISED, overrelief=RIDGE, fg='white', command= lambda: show(')'))
b_e.place(x=360, y=0)



        #FILA 2
b_exponencial2 = Button(frame_scientific, text='π', width=11, height=2, bg=dark, font='Ivy 13 bold',
                        relief=RAISED, overrelief=RIDGE, fg='white', command= lambda: show('π'))
b_exponencial2.place(x=0, y=52)

b_exponencial2 = Button(frame_scientific, text='EXP', width=11, height=2, bg=dark, font='Ivy 13 bold',
                        relief=RAISED, overrelief=RIDGE, fg='white', command= lambda: show('*10**('))
b_exponencial2.place(x=120, y=52)

b_exponencial2 = Button(frame_scientific, text='ANS', width=11, height=2, bg=dark, font='Ivy 13 bold',
                        relief=RAISED, overrelief=RIDGE, fg='white', command=ans)
b_exponencial2.place(x=240, y=52)

b_exponencial2 = Button(frame_scientific, text='√', width=11, height=2, bg=dark, font='Ivy 13 bold',
                        relief=RAISED, overrelief=RIDGE, fg='white', command= lambda: show('√('))
b_exponencial2.place(x=360, y=52)



    #BOTÕES CONVERTER E FÓRMULAS
b_convert = Button(frame, text='$', width=1, height=1, bg=black, font='Ivy 13 bold',
                        relief=RAISED, overrelief=RIDGE, bd=0, fg='white', command=convertbtn, cursor='hand2')
b_convert.place(x=10, y=120)

b_formula = Button(frame, text='Δ', width=1, height=1, bg=black, font='Ivy 13 bold',
                        relief=RAISED, overrelief=RIDGE, bd=0, fg='white', command=formula, cursor='hand2')
b_formula.place(x=30, y=120)




myLabel = Label()
myLabel2 = Label()
myLabel3 = Label()
myLabel4 = Label()
myLabel5 = Label()
myLabel6 = Label()
fra = Frame()
fra2 = Frame()

window.mainloop()