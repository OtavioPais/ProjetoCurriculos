from tkinter import * # para importa todos os classes, funções, constantes do Tkinter *
import tkinter as tk # Para utilização geral do projeto *
from tkinter import messagebox # Para utiizar as mensagens de resposta *
from candidato import Candidato # Para gerar e apontar os campos que serão utilizados durante o processo do programa *
from database import Database # Para utilizar,importar e enviar os dados ao BD *
from pdf_gerador import PDFGerador # Para utilizar e gerar os PDF´s *
from tkinter import ttk # para utilizar widgets temáticos do Tkinter *
from PIL import Image, ImageTk # Para utilizar e importar as imagens *
import subprocess # Urilizado para abrir aplicativos externos e executar comandos de sistema *
import os # Para interagir diretamente com o S.O e fazer operações diretas *

xampp_path = "C:/xampp/xampp_start.exe"

if os.path.exists(xampp_path):
    try:
        subprocess.run([xampp_path, "startapache"], check=True)
        subprocess.run([xampp_path, "startmysql"], check=True)
        print("XAMPP iniciado com sucesso! Apache e MySQL estão rodando.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao iniciar o XAMPP: {e}")
else:
    print(f"O caminho para o executável XAMPP ({xampp_path}) não foi encontrado.")

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Currículo da Startup")
        self.root.geometry("323x700")
        self.definir_imagem_formulario()
        root.configure(bg='white')

    def definir_imagem_formulario(self):
        imagem_fundo = Image.open("Imagens\\formulario.png")
        foto_fundo = ImageTk.PhotoImage(imagem_fundo)
        texto_fundo = Label(self.root, image=foto_fundo)
        texto_fundo.image = foto_fundo
        texto_fundo.place(x=0, y=0, relwidth=1, relheight=1)

        self.nome_entrar = tk.Entry(root, width=35, justify=CENTER, bd=3, relief=SOLID)
        self.nome_entrar.place(x=52, y=120)

        self.telefone_entrar = tk.Entry(root, width=35, justify=CENTER, bd=3, relief=SOLID)
        self.telefone_entrar.place(x=52, y=180)

        self.minibio_entrar = tk.Entry(root, width=35, justify=CENTER, bd=3, relief=SOLID)
        self.minibio_entrar.place(x=52, y=240)

        self.nota_entrevista_entrar = tk.Entry(root, width=35, justify=CENTER, bd=3, relief=SOLID)
        self.nota_entrevista_entrar.place(x=52, y=310)

        self.nota_teorico_entrar = tk.Entry(root, width=35, justify=CENTER, bd=3, relief=SOLID)
        self.nota_teorico_entrar.place(x=52, y=375)

        self.nota_pratica_entrar = tk.Entry(root, width=35, justify=CENTER, bd=3, relief=SOLID)
        self.nota_pratica_entrar.place(x=52, y=440)

        self.nota_softskills_entrar = tk.Entry(root, width=35, justify=CENTER, bd=3, relief=SOLID)
        self.nota_softskills_entrar.place(x=52, y=505)
        
        tk.Button(root, text="Cadastrar Candidato", width=32, height=2, justify=CENTER, bg="#004aad", command=self.cad_candidato).place(x=44, y=548)
        tk.Button(root, text="Gerar Relatório", width=32, height=2, justify=CENTER, bg="yellow", command=self.gerar_relatorio_completo).place(x=45, y=595)
        tk.Button(root, text="Buscar Candidatos", width=32, height=2, justify=CENTER, bg="red", command=self.abrir_janela_pesquisa).place(x=45, y=645)
        tk.Button(root, text="X", width=3, justify=CENTER, bg="red", command=self.sair).place(x=278, y=15)  

    def cad_candidato(self):
        nome = self.nome_entrar.get()
        telefone = self.telefone_entrar.get()
        minibio = self.minibio_entrar.get()
        nota_entrevista = int(self.nota_entrevista_entrar.get())
        nota_teorico = int(self.nota_teorico_entrar.get())
        nota_pratica = int(self.nota_pratica_entrar.get())
        nota_softskills = int(self.nota_softskills_entrar.get())

        self.nome_entrar.delete(0, END)
        self.telefone_entrar.delete(0, END)
        self.minibio_entrar.delete(0, END)
        self.nota_entrevista_entrar.delete(0, END)
        self.nota_teorico_entrar.delete(0, END)
        self.nota_pratica_entrar.delete(0, END)
        self.nota_softskills_entrar.delete(0, END)

        if not nome or not telefone or not minibio or not nota_entrevista or not nota_teorico or not nota_pratica or not nota_softskills or not NONE:
            messagebox.showerror("Campos em Branco", "Por favor, preencha todos os campos para cadastrar !")
        else:
            novo_candidato = Candidato(nome, telefone, minibio, nota_entrevista, nota_teorico, nota_pratica, nota_softskills)
            db.cad_candidato(novo_candidato)     
            messagebox.showinfo("Cadastro de Candidato", "Candidato cadastrado com sucesso !")

    def gerar_relatorio_completo(self):
        candidatos_compativeis = db.busca_candidatos(0, 0, 0, 0)
        gerar_pdf.gerar_relatorio_completo(candidatos_compativeis)

    def abrir_janela_pesquisa(self):
        janela_pesquisa = tk.Toplevel(self.root)
        janela_pesquisa.title("Pesquisar Candidatos")
        janela_pesquisa.geometry("323x700")
        self.definir_imagem_selecao(janela_pesquisa)

        self.min_nota_entrevista_entrar = tk.Entry(janela_pesquisa, width=35, justify=CENTER, bd=3, relief=SOLID)
        self.min_nota_entrevista_entrar.place(x=52, y=120)

        self.min_nota_teorico_entrar = tk.Entry(janela_pesquisa, width=35, justify=CENTER, bd=3, relief=SOLID)
        self.min_nota_teorico_entrar.place(x=52, y=180)

        self.min_nota_pratica_entrar = tk.Entry(janela_pesquisa, width=35, justify=CENTER, bd=3, relief=SOLID)
        self.min_nota_pratica_entrar.place(x=52, y=240)

        self.min_nota_softskills_entrar = tk.Entry(janela_pesquisa, width=35, justify=CENTER, bd=3, relief=SOLID)
        self.min_nota_softskills_entrar.place(x=52, y=310)

        tk.Button(janela_pesquisa, text="Pesquisar Candidatos", width=32, height=2, justify=CENTER, bg="#8c52ff", command=self.busca_candidatos).place(x=45, y=370)
        tk.Button(janela_pesquisa, text="Retornar", width=32, height=2, justify=CENTER, bg="red", command=janela_pesquisa.destroy).place(x=45, y=435)
        tk.Button(janela_pesquisa, text="X", width=3, justify=CENTER, bg="red", command=janela_pesquisa.destroy).place(x=278, y=15)

    def definir_imagem_selecao(self, janela):
        imagem_fundo = Image.open("Imagens\\selecao.png")
        foto_fundo = ImageTk.PhotoImage(imagem_fundo)
        texto_fundo = Label(janela, image=foto_fundo)
        texto_fundo.image = foto_fundo
        texto_fundo.place(x=0, y=0, relwidth=1, relheight=1)

    def busca_candidatos(self):
        min_nota_entrevista = int(self.min_nota_entrevista_entrar.get())
        min_nota_teorico = int(self.min_nota_teorico_entrar.get())
        min_nota_pratica = int(self.min_nota_pratica_entrar.get())
        min_nota_softskills = int(self.min_nota_softskills_entrar.get())
        candidatos_compativeis = db.busca_candidatos(min_nota_entrevista, min_nota_teorico, min_nota_pratica, min_nota_softskills)

        if candidatos_compativeis:
            self.mostrar_candidato(candidatos_compativeis)
        else:
            messagebox.showwarning("Pesquisa de Candidatos", "Nenhum candidato compatível com o requisito da vaga encontrado !")

        self.min_nota_entrevista_entrar.delete(0, END)
        self.min_nota_teorico_entrar.delete(0, END)
        self.min_nota_pratica_entrar.delete(0, END)
        self.min_nota_softskills_entrar.delete(0, END)

    def mostrar_candidato(self, candidatos):
        self.root = tk.Tk()
        self.root.geometry("1050x700")
        self.root.title("Candidatos Compatíveis")
        self.tabControl = ttk.Notebook(self.root)
        self.tabControl.pack(expand=1, fill="both")

        for i, candidato in enumerate(candidatos):
            candidato_frame = ttk.Frame(self.tabControl)
            self.tabControl.add(candidato_frame, text=f"CNDT {i + 1}")

            tk.Label(candidato_frame, text=f"Nome: {candidato[1]}").pack()
            tk.Label(candidato_frame, text=f"Telefone: {candidato[2]}").pack()
            tk.Label(candidato_frame, text=f"Minibio: {candidato[3]}").pack()
            tk.Label(candidato_frame, text=f"Nota Entrevista: {candidato[4]}").pack()
            tk.Label(candidato_frame, text=f"Nota Prova Teórica: {candidato[5]}").pack()
            tk.Label(candidato_frame, text=f"Nota Prova Prática: {candidato[6]}").pack()
            tk.Label(candidato_frame, text=f"Nota Soft Skills: {candidato[7]}").pack()

        botao_fechar = tk.Button(self.root, width=10, justify=CENTER, text="Sair", bg="red", command=self.root.destroy) 
        botao_fechar.pack(pady=20)
    
    def sair(self):
        if self.root:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    db = Database()
    gerar_pdf = PDFGerador()
    app = GUI(root)
    root.mainloop()