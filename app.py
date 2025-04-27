import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


arquivos_abertos = {}

def criar_arquivo():# def define uma função, no caso criar arquivo
    path = filedialog.asksaveasfilename()#armazema esta função na variavel path
    if path:
        with open(path, 'w') as f:
            f.write("")
        messagebox.showinfo("Sucesso", f"Arquivo criado: {path}")

def abrir_arquivo():
    path = filedialog.askopenfilename()
    if path:
        if arquivos_abertos.get(path):
            messagebox.showwarning("Erro", "Arquivo já está aberto!")
            return
        arquivos_abertos[path] = True
        with open(path, 'r') as f:
            conteudo = f.read()
        messagebox.showinfo("Conteúdo", conteudo)

def fechar_arquivo():
    path = filedialog.askopenfilename()
    if path and arquivos_abertos.get(path):
        arquivos_abertos[path] = False
        messagebox.showinfo("Sucesso", "Arquivo fechado!")
    else:
        messagebox.showwarning("Erro", "Arquivo não está aberto.")

def deletar_arquivo():
    path = filedialog.askopenfilename()
    if path:
        if arquivos_abertos.get(path):
            messagebox.showwarning("Erro", "Arquivo está aberto e não pode ser deletado!")
            return
        os.remove(path)
        messagebox.showinfo("Sucesso", "Arquivo deletado!")

def renomear_arquivo():
    path = filedialog.askopenfilename()
    if path:
        nova_nome = filedialog.asksaveasfilename()
        if nova_nome:
            os.rename(path, nova_nome)
            messagebox.showinfo("Sucesso", "Arquivo renomeado!")

def copiar_arquivo():
    path = filedialog.askopenfilename()
    if path:
        destino = filedialog.asksaveasfilename()
        if destino:
            shutil.copy(path, destino)
            messagebox.showinfo("Sucesso", "Arquivo copiado!")

def listar_arquivos():
    pasta = filedialog.askdirectory()
    if pasta:
        arquivos = os.listdir(pasta)
        messagebox.showinfo("Arquivos", "\n".join(arquivos))

def modificar_atributo():
    path = filedialog.askopenfilename()
    if path:
        # Exemplo: Tornar arquivo somente leitura
        os.chmod(path, 0o444)  # leitura apenas
        messagebox.showinfo("Sucesso", "Arquivo agora é somente leitura!")

# Criar interface
root = tk.Tk()
root.title("Simulador de Sistema Operacional")

tk.Button(root, text="Criar Arquivo", command=criar_arquivo).pack(fill="x")
tk.Button(root, text="Abrir Arquivo", command=abrir_arquivo).pack(fill="x")
tk.Button(root, text="Fechar Arquivo", command=fechar_arquivo).pack(fill="x")
tk.Button(root, text="Deletar Arquivo", command=deletar_arquivo).pack(fill="x")
tk.Button(root, text="Renomear Arquivo", command=renomear_arquivo).pack(fill="x")
tk.Button(root, text="Copiar Arquivo", command=copiar_arquivo).pack(fill="x")
tk.Button(root, text="Listar Arquivos", command=listar_arquivos).pack(fill="x")
tk.Button(root, text="Modificar Atributo", command=modificar_atributo).pack(fill="x")

root.mainloop()
