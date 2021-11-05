from tkinter import *
from tkinter import ttk


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


wind = Tk()
wind.title('Gerador de senhas Tk')
wind.geometry('310x390')
wind.configure(bg=cor_fundo)

#-------------------------------------------------------------------------
frm_c = Frame(wind, width=310, height=150, bg=cor_frmc, relief='flat')
frm_c.grid(row=0, column=0, sticky=NSEW)

frm_b = Frame(wind, width=310, height=240, bg=cor_frmb, relief='flat')
frm_b.grid(row=1, column=0, sticky=NSEW)

#-------------------------------------------------------------------------
lbl_title = Label(frm_c, text='GERADOR DE SENHAS', bg=cor_frmc, width=36, anchor=CENTER)
lbl_title.place(x=0, y=0)


btn_sair = Button(frm_b, command=sair, text='Sair', bg=cor_btn)
btn_sair.place(x=20, y=170)


wind.mainloop()
