from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import string
import random

"""
Projeto desenvolvido em aula, cujo objetivo principal é a prática da programação na linguagem
python, neste caso vamos usar uma interface gráfica tkinter, para melhor visualizar a saída do
código.

"""

cor_fundo = '#160c01'
cor_frmc = '#efaf59'
cor_frmb = '#9c8566'
cor_btn = '#82679c'

def sair():
    wind.destroy()

def gerar_senha():
    alpha_maiusc = string.ascii_uppercase
    alpha_minusc = string.ascii_lowercase
    numeros = '0123456789'
    simbolos = '[]{_/*&%#@!+}^:;<>?=()"-'

    global mesclar

    # mesclar = alpha_maiusc + alpha_minusc + numeros + simbolos

    if estado_1.get() == alpha_maiusc:
        mesclar = alpha_maiusc
    else:
        pass

    if estado_2.get() == alpha_minusc:
        mesclar = mesclar + alpha_minusc
    else:
        pass

    if estado_3.get() == numeros:
        mesclar = mesclar + numeros
    else:
        pass

    if estado_4.get() == simbolos:
        mesclar = mesclar + simbolos
    else:
        pass
    
    tamanho = int(spin.get())
    senha = "".join(random.sample(mesclar, tamanho))

    lbl_nome['text'] = senha


wind = Tk()
wind.title('Gerador de senhas Tk')
wind.geometry('310x390')
wind.configure(bg=cor_fundo)

#--------------------------------------------------------------------------------------
frm_c = Frame(wind, width=310, height=100, bg=cor_frmc, relief='flat')
frm_c.grid(row=0, column=0, sticky=NSEW)

frm_b = Frame(wind, width=310, height=290, bg=cor_frmb, relief='flat')
frm_b.grid(row=1, column=0, sticky=NSEW)

#---------------------------------------------------------------------------------------
img = Image.open('key2.png')
img = img.resize((30, 30), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
lbl_title = Label(frm_c, height=60, image=img, compound=LEFT, padx=10, pady=10, bg=cor_frmc, anchor=NW)
lbl_title.place(x=4, y=0)

lbl_tn = Label(frm_c, height=60, text='GERADOR DE SENHAS', fg='white', bg=cor_frmc, width=20, anchor=NW, font=('Arial 15 bold'))
lbl_tn.place(x=45, y=0)


btn_sair = Button(frm_b, command=sair, text='Sair', bg=cor_frmb)
btn_sair.place(x=20, y=220)

btn_gerar = Button(frm_b, command=gerar_senha, text='Gerar senha', bg=cor_frmb)
btn_gerar.place(x=90, y=220)

lbl_nome = Label(frm_b, height=2, text='---', fg='white', bg=cor_frmc, width=20)
lbl_nome.place(x=20, y=10)


lbl_copiar = Button(frm_b, height=1, text='Copiar', fg='white', bg=cor_frmc, width=8)
lbl_copiar.place(x=192, y=10)

var = IntVar()
var.set(0)
spin = Spinbox(frm_b, from_=0, to=20, width=5, textvariable=var)
spin.place(x=20, y=50)

alpha_maiusc = string.ascii_uppercase
alpha_minusc = string.ascii_lowercase
numeros = '0123456789'
simbolos = '[]{_/*&%#@!+}^:;<>?=()"-'

#  letras maúsculas
estado_1 = StringVar()
estado_1.set(False)
chk_1 = Checkbutton(frm_b, text='ABC maiúsculo', width=13, var=estado_1, onvalue=alpha_maiusc, relief='flat', offvalue='off', bg=cor_frmb)
chk_1.place(x=20, y=79)

#  letras minúsculas
estado_2 = StringVar()
estado_2.set(False)
chk_2 = Checkbutton(frm_b, text='abc minúsculo', width=13, var=estado_2, onvalue=alpha_minusc, relief='flat', offvalue='off', bg=cor_frmb)
chk_2.place(x=20, y=109)

#  letras nimeros
estado_3 = StringVar()
estado_3.set(False)
chk_3 = Checkbutton(frm_b, text='números', width=9, var=estado_3, onvalue=numeros, relief='flat', offvalue='off', bg=cor_frmb)
chk_3.place(x=20, y=139)

#  letras simbolos
estado_4 = StringVar()
estado_4.set(False)
chk_4 = Checkbutton(frm_b, text='símbolos', width=9, var=estado_4, onvalue=simbolos, relief='flat', offvalue='off', bg=cor_frmb)
chk_4.place(x=20, y=169)



wind.mainloop()
