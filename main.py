import tkinter as tk
from tkinter import *
import os
from time import strftime

root = tk.Tk()
root.title('Seu Relógio')
root.geometry("600x300")
root.maxsize(600,320)
root.minsize(600,320)
root.configure(background='#1d1d1d')

def get_saudacao():
    nome_usuario = os.getlogin()
    saudacao.config(text='Olá, ' + nome_usuario)
def get_data():
    data_atual = strftime(' %a, %d %b %Y')
    data.config(text=data_atual)
def get_horas():
    hora_atual = strftime('%H:%M:%S')
    horas.config(text=hora_atual)
    horas.after(1000, get_horas)

tela = tk.Canvas(root, width=600, height=60, bg='#1d1d1d', bd=0, highlightthickness=0, relief='ridge')
tela.pack()