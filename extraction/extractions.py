#This library would consist all the different erxtraction methods from various sources

import pandas as pd
import PyPDF2
import xlsxwriter as xlsx

class invoke_extraction:
    def __init__(self,document_name_path):
        self.document_name_path=document_name_path
        self.document_name=document_name_path.rsplit('/',1)[1]
        self.document_path=document_name_path.rsplit('/',1)[0]
        self.ext=self.document_name.split('.')[1] #this will be  either pdf, csv, xlsx

    def extract_text_from_pdf(self):
        text = ""
        
        try:
            with open(self.document_name_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text()
            
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("An error occurred:", str(e))
        
        return text


read_pdf=invoke_extraction('/Users/suryansh/Documents/FiiDii.pdf')
text=read_pdf.extract_text_from_pdf()
print(text)
