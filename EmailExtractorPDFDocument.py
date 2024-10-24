import re
import PyPDF2

def extrair_emails_de_pdf(arquivo_pdf):
    emails = []
    
    with open(arquivo_pdf, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            text = page.extractText()
            padrao = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            emails.extend(re.findall(padrao, text))
    
    return emails

# Exemplo de uso
arquivo_pdf = "exemplo.pdf"  # Substitua pelo nome do seu arquivo PDF
emails_encontrados = extrair_emails_de_pdf(arquivo_pdf)
print("E-mails encontrados no PDF:")
for email in emails_encontrados:
    print(email)
