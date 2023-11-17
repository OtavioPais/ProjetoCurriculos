import os # Para interagir diretamente com o S.O e fazer operações diretas *
from database import Database
from fpdf import FPDF
from tkinter import messagebox

class PDFGerador:
    def gerar_relatorio_completo(self, candidatos):
        resposta = messagebox.askquestion("Gerar Relatório", "Deseja Gerar o Relatório Completo ?")
        if resposta == "yes":
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            for candidato in candidatos:
                pdf.cell(0, 10, f"ID do Entrevistado: {candidato[0]}", ln=True)
                pdf.cell(0, 10, f"Nome: {candidato[1]}", ln=True)
                pdf.cell(0, 10, f"Telefone: {candidato[2]}", ln=True)
                pdf.cell(0, 10, f"Minibio: {candidato[3]}", ln=True)
                pdf.cell(0, 10, f"Nota Entrevista: {candidato[4]}", ln=True)
                pdf.cell(0, 10, f"Nota Prova Teórica: {candidato[5]}", ln=True)
                pdf.cell(0, 10, f"Nota Prova Prática: {candidato[6]}", ln=True)
                pdf.cell(0, 10, f"Nota Soft Skills: {candidato[7]}", ln=True)
                pdf.ln(10)
            output_dir = "Relatorios/Completo"
            os.makedirs(output_dir, exist_ok=True)
            output_file = os.path.join(output_dir, "Relatorio_Completo_Atualizado.pdf")
            pdf.output(output_file)
            messagebox.showinfo("Relatório Completo", "Relatório Completo Gerado com Sucesso !")
        else:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            for candidato in candidatos:
                pdf.cell(0, 10, f"Nome: {candidato[1]}", ln=True)
                pdf.cell(0, 10, f"Nota Entrevista: {candidato[4]}", ln=True)
                pdf.cell(0, 10, f"Nota Prova Teórica: {candidato[5]}", ln=True)
                pdf.cell(0, 10, f"Nota Prova Prática: {candidato[6]}", ln=True)
                pdf.cell(0, 10, f"Nota Soft Skills: {candidato[7]}", ln=True)
                pdf.ln(10)
            output_dir = "Relatorios/Resumido"
            os.makedirs(output_dir, exist_ok=True)
            output_file = os.path.join(output_dir, "Relatorio_Resumido_Atualizado.pdf")
            pdf.output(output_file)
            messagebox.showinfo("Relatório Resumido", "Relatório Resumido Gerado com Sucesso !")

db = Database()
pdf_generator = PDFGerador()