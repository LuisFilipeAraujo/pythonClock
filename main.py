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

tela = tk.Canvas(root, width=600, height=60, bg='#1d1d1d', bd=0, highlightthickness=0, relief='ridge')
tela.pack()