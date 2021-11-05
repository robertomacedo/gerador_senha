from tkinter import *
from tkinter import ttk

"""
Projeto desenvolvido em aula, cujo objetivo principal é a prática da programação na linguagem
python, nest caso vamos usar uma interface gráfica que é o tkinter, para melhor visualização
da saída do código.

"""
cor_fundo = '#160c01'
cor_frmc = '#efaf59'
cor_frmb = '#9c8566'


wind = Tk()
wind.title('Gerador de senhas Tk')
wind.geometry('310x390')
wind.configure(bg=cor_fundo)

frm_c = Frame(wind, width=310, height=150, bg=cor_frmc, relief='flat')
frm_c.grid(row=0, column=0, sticky=NSEW)

frm_b = Frame(wind, width=310, height=240, bg=cor_frmb, relief='flat')
frm_b.grid(row=1, column=0, sticky=NSEW)


wind.mainloop()
